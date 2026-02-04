import os
import hashlib
import json
import logging
import re
import time
from openai import OpenAI, APIError
from mkdocs.config import Config
from mkdocs.structure.pages import Page
from mkdocs.structure.files import Files

# ================= 配置区域 =================

# 1. 缓存文件
CACHE_FILE = "ai_summary_cache.json"

# 2. API 设置 (使用 DeepSeek)
# 请确保你在终端设置了环境变量: export DEEPSEEK_API_KEY="sk-你的密钥"
API_KEY = os.environ.get("DEEPSEEK_API_KEY")

# 初始化 OpenAI 客户端 (适配 DeepSeek)
client = None
if API_KEY:
    client = OpenAI(
        api_key=API_KEY,
        base_url="https://api.deepseek.com"
    )

# 全局变量
TOTAL_WORDS = 0
log = logging.getLogger("mkdocs")

# ================= 辅助函数 =================

def load_cache():
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}

def save_cache(cache):
    with open(CACHE_FILE, 'w', encoding='utf-8') as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

def get_ai_summary(text):
    """
    使用 OpenAI SDK 调用 DeepSeek 生成总结
    """
    if not client:
        log.warning("⚠️ 未检测到 DEEPSEEK_API_KEY，跳过 AI 总结。")
        return None

    # 提示词
    prompt = f"请用一段简练、幽默的中文总结以下技术文章的核心内容，字数控制在100字以内，不要使用'本文'开头，直接概括：\n\n{text[:3000]}"
    
    # 重试机制
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": "你是一个专业的文章摘要助手。"},
                    {"role": "user", "content": prompt}
                ],
                stream=False,
                temperature=0.7
            )
            
            # 获取内容
            content = response.choices[0].message.content
            if content:
                # DeepSeek 速度很快，但为了保险起见，稍微停顿 0.5 秒
                time.sleep(0.5)
                return content

        except Exception as e:
            # 捕获所有 SDK 抛出的异常 (如认证失败、限流、网络超时等)
            log.warning(f"❌ API 请求失败 (尝试 {attempt+1}/{max_retries}): {e}")
            time.sleep(2) # 出错后等待 2 秒再重试
    
    log.error("🚫 多次重试失败，跳过此文章。")
    return None

def count_words_in_text(text):
    """统计中英文混合字数"""
    clean_text = re.sub(r'<[^>]+>', '', text) 
    clean_text = re.sub(r'[#*`\[\]\(\)!>\-]', '', clean_text)
    zh_chars = len(re.findall(r'[\u4e00-\u9fa5]', clean_text))
    en_words = len(re.findall(r'\b\w+\b', clean_text))
    return zh_chars + en_words

# ================= MkDocs Hooks =================

def on_config(config: Config):
    global TOTAL_WORDS
    TOTAL_WORDS = 0
    if not os.path.exists(CACHE_FILE):
        save_cache({})

def on_page_markdown(markdown: str, page: Page, config: Config, files: Files):
    global TOTAL_WORDS

    # 1. 排除主页和无 URL 页面
    if page.meta.get('template') == 'home' or page.url == '':
        return markdown

    # 2. 统计字数
    word_count = count_words_in_text(markdown)
    TOTAL_WORDS += word_count
    page.meta['word_count'] = word_count

    # 3. 如果已有 summary，跳过
    if 'summary' in page.meta:
        return markdown

    # 4. AI 总结处理
    cache = load_cache()
    content_hash = hashlib.md5(markdown.encode('utf-8')).hexdigest()

    summary = ""
    
    if content_hash in cache:
        summary = cache[content_hash]
    else:
        log.info(f"🤖 正在调用 DeepSeek 为 [{page.title}] 生成总结...")
        ai_result = get_ai_summary(markdown)
        if ai_result:
            summary = ai_result
            cache[content_hash] = summary
            save_cache(cache)

    # 5. 插入 Admonition 块
    if summary:
        ai_block = f"""
!!! abstract "AI 自动摘要"
    {summary}
"""
        return ai_block + "\n" + markdown
    
    return markdown

def on_env(env, config, files):
    global TOTAL_WORDS
    # 注入全局变量
    env.globals['total_words'] = TOTAL_WORDS
    formatted = f"{TOTAL_WORDS / 10000:.1f}万" if TOTAL_WORDS > 10000 else str(TOTAL_WORDS)
    env.globals['total_words_formatted'] = formatted
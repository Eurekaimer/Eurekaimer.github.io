import os
import requests

# 替换为你的 API Key
API_KEY = "AIzaSyDkwDvljWl558a2cqISm90HdhT4rTcdvHg"

def list_models():
    url = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        models = response.json().get('models', [])
        print("✅ 你的 API Key 支持以下模型：")
        for m in models:
            # 只列出支持生成内容的模型
            if "generateContent" in m.get("supportedGenerationMethods", []):
                print(f" - {m['name'].replace('models/', '')}")
    else:
        print(f"❌ 获取失败: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    list_models()
# Copyright (c) 2024 Eurekaimer
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

import json
import os
import time  # Used for cache management and time formatting
import requests
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options

class CodeforcesPlugin(BasePlugin):
    
    config_scheme = (
        ('cache_dir', config_options.Type(str, default='.cache/codeforces')),
        ('cache_ttl', config_options.Type(int, default=3600)),  # 缓存时间，默认1小时
        ('default_username', config_options.Type(str, default='')),
        ('default_width', config_options.Type(str, default='100%')),
        ('default_theme', config_options.Type(str, default='light')),  # light, dark
    )
    
    def on_config(self, config):
        """插件初始化时调用"""
        # 确保缓存目录存在
        self.cache_dir = os.path.join(config['docs_dir'], '..', self.config['cache_dir'])
        os.makedirs(self.cache_dir, exist_ok=True)
        # 移除可能的CSS引用，确保只使用内联样式
        if 'extra_css' in config:
            css_to_remove = []
            for css in config['extra_css']:
                if 'codeforces.css' in css:
                    css_to_remove.append(css)
            for css in css_to_remove:
                config['extra_css'].remove(css)
        return config
    
    def on_page_markdown(self, markdown, page, config, files):
        """处理页面中的Markdown内容"""
        import re
        
        # 匹配codeforces标签：{% codeforces username="username" width="100%" theme="light" %}
        pattern = r'\{%\s*codeforces\s*(.*?)\s*%\}'
        
        def replace_codeforces_tag(match):
            # 解析参数
            params = {}
            for param in re.findall(r'(\w+)="([^"]+)"', match.group(1)):
                params[param[0]] = param[1]
            
            # 使用配置或默认值
            username = params.get('username', self.config['default_username'])
            width = params.get('width', self.config['default_width'])
            theme = params.get('theme', self.config['default_theme'])
            
            if not username:
                return '<div class="codeforces-error">错误：必须指定Codeforces用户名</div>'
            
            # 获取用户数据
            user_data = self._get_user_data(username)
            if not user_data:
                return f'<div class="codeforces-error">无法获取用户 {username} 的数据</div>'
            
            # 生成卡片HTML
            return self._generate_card_html(user_data, width, theme)
        
        # 替换所有codeforces标签
        return re.sub(pattern, replace_codeforces_tag, markdown)
    
    def on_post_build(self, config):
        """构建完成后调用，用于清理过期缓存"""
        self._cleanup_cache()
        return config
    
    def _get_user_data(self, username):
        """从Codeforces API获取用户数据，带有缓存机制"""
        cache_file = os.path.join(self.cache_dir, f"{username}.json")
        
        # 检查缓存是否有效
        if os.path.exists(cache_file):
            cache_time = os.path.getmtime(cache_file)
            if time.time() - cache_time < self.config['cache_ttl']:
                try:
                    with open(cache_file, 'r', encoding='utf-8') as f:
                        return json.load(f)
                except:
                    pass
        
        # 从API获取数据
        try:
            # 获取用户基本信息
            user_info_url = f"https://codeforces.com/api/user.info?handles={username}"
            user_info_response = requests.get(user_info_url, timeout=10)
            user_info = user_info_response.json()
            
            if user_info['status'] != 'OK':
                return None
            
            user = user_info['result'][0]
            
            # 获取用户最近提交
            submissions_url = f"https://codeforces.com/api/user.status?handle={username}&from=1&count=5"
            submissions_response = requests.get(submissions_url, timeout=10)
            submissions_data = submissions_response.json()
            
            if submissions_data['status'] == 'OK':
                user['recent_submissions'] = submissions_data['result'][:3]  # 最近3次提交
                
                # 计算已解决问题的总数（去重）
                solved_problems = set()
                for submission in submissions_data['result']:
                    if submission.get('verdict') == 'OK':
                        problem = submission.get('problem', {})
                        problem_key = f"{problem.get('contestId', '')}_{problem.get('index', '')}"
                        solved_problems.add(problem_key)
                
                # 获取更多提交记录以计算完整的已解决问题数
                # Codeforces API每次最多返回1000条记录，分批次获取
                from_num = 6
                while True:
                    more_submissions_url = f"https://codeforces.com/api/user.status?handle={username}&from={from_num}&count=1000"
                    more_submissions_response = requests.get(more_submissions_url, timeout=10)
                    more_submissions_data = more_submissions_response.json()
                    
                    if more_submissions_data['status'] != 'OK' or not more_submissions_data['result']:
                        break
                    
                    for submission in more_submissions_data['result']:
                        if submission.get('verdict') == 'OK':
                            problem = submission.get('problem', {})
                            problem_key = f"{problem.get('contestId', '')}_{problem.get('index', '')}"
                            solved_problems.add(problem_key)
                    
                    from_num += 1000
                    # 避免请求过于频繁
                    time.sleep(0.5)
                
                user['solvedCount'] = len(solved_problems)
            else:
                user['recent_submissions'] = []
                user['solvedCount'] = 0
            
            # 获取用户参与的比赛
            contests_url = f"https://codeforces.com/api/user.rating?handle={username}"
            contests_response = requests.get(contests_url, timeout=10)
            contests_data = contests_response.json()
            
            if contests_data['status'] == 'OK':
                user['contests'] = contests_data['result'][-3:]  # 最近3次比赛
            else:
                user['contests'] = []
            
            # 保存到缓存
            with open(cache_file, 'w', encoding='utf-8') as f:
                json.dump(user, f, ensure_ascii=False, indent=2)
            
            return user
        except Exception as e:
            print(f"获取Codeforces用户数据错误: {e}")
            return None
    
    def _generate_card_html(self, user_data, width, theme):
        """生成美观的用户卡片HTML"""
        # 导入time模块以确保可用
        import time
        
        # 根据rating确定颜色和等级
        rating = user_data.get('rating', 0)
        rank = user_data.get('rank', 'unrated')
        
        # Codeforces颜色等级
        color_map = {
            'newbie': '#808080',
            'pupil': '#008000',
            'specialist': '#03a89e',
            'expert': '#0000ff',
            'candidate master': '#aa00aa',
            'master': '#ff8c00',
            'international master': '#ff8c00',
            'grandmaster': '#ff0000',
            'international grandmaster': '#ff0000',
            'legendary grandmaster': '#ff0000'
        }
        
        color = color_map.get(rank.lower(), '#808080')
        
        # 确保registrationTimeSeconds存在且有效
        reg_time = user_data.get('registrationTimeSeconds', 0)
        try:
            reg_date = time.strftime('%Y-%m-%d', time.localtime(reg_time)) if reg_time > 0 else '未知'
        except:
            reg_date = '未知'
        
        # 生成卡片HTML，使用完整的内联样式确保显示正确
        html = []
        html.append('<div style="width: {width}; margin: 1rem 0; border: 1px solid #e0e0e0; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 8px rgba(0,0,0,0.1); background-color: white;">'.format(width=width))
        html.append('<div style="display: flex; align-items: center; padding: 16px; background-color: #f8f9fa; border-bottom: 2px solid {color};">'.format(color=color))
        html.append('<div style="margin-right: 16px;">')
        html.append('<img src="https://cdn-icons-png.flaticon.com/512/6132/6132222.png" alt="Codeforces" width="40" height="40">')
        html.append('</div>')
        html.append('<div>')
        html.append('<h3 style="margin: 0 0 4px 0; font-size: 1.4rem; font-weight: 600;">{handle}</h3>'.format(handle=user_data.get('handle', 'Unknown')))
        html.append('<div style="color: {color}; font-size: 1rem; font-weight: 500;">'.format(color=color))
        html.append('{rank} • {rating} rating'.format(rank=rank, rating=rating))
        html.append('</div>')
        html.append('</div>')
        html.append('</div>')
        html.append('<div style="padding: 20px;">')
        html.append('<div style="display: flex; flex-wrap: wrap; gap: 20px; margin-bottom: 20px; padding-bottom: 20px; border-bottom: 1px solid #e0e0e0;">')
        html.append('<div style="display: flex; flex-direction: column; align-items: center; min-width: 80px;">')
        html.append('<span style="font-size: 0.9rem; color: #666;">已解决问题</span>')
        html.append('<span style="font-size: 1.2rem; font-weight: 600;">{solved}</span>'.format(solved=user_data.get('solvedCount', 0)))
        html.append('</div>')
        html.append('<div style="display: flex; flex-direction: column; align-items: center; min-width: 80px;">')
        html.append('<span style="font-size: 0.9rem; color: #666;">贡献值</span>')
        html.append('<span style="font-size: 1.2rem; font-weight: 600;">{contribution}</span>'.format(contribution=user_data.get('contribution', 0)))
        html.append('</div>')
        html.append('<div style="display: flex; flex-direction: column; align-items: center; min-width: 80px;">')
        html.append('<span style="font-size: 0.9rem; color: #666;">注册时间</span>')
        html.append('<span style="font-size: 1.2rem; font-weight: 600;">{reg_date}</span>'.format(reg_date=reg_date))
        html.append('</div>')
        html.append('</div>')
        html = ''.join(html)
        
        # 添加最近提交记录
        if user_data.get('recent_submissions'):
            html += ''.join([
                '<div style="margin-bottom: 20px;">',
                '<h4 style="margin: 0 0 12px 0; font-size: 1.1rem; font-weight: 600;">最近提交</h4>',
                '<ul style="list-style: none; padding: 0; margin: 0;">'
            ])
            for sub in user_data['recent_submissions']:
                problem = sub.get('problem', {})
                verdict = sub.get('verdict', '').lower()
                status_text = '✓ 已通过' if 'accepted' in verdict else '✗ 未通过'
                border_color = '#4caf50' if 'accepted' in verdict else '#f44336'
                
                html += '<li style="padding: 8px 12px; margin-bottom: 6px; border-radius: 4px; background-color: #f5f5f5; display: flex; justify-content: space-between; align-items: center; border-left: 4px solid {border_color};">' \
                       '<span style="font-weight: 500; flex: 1;">{problem_name}</span>' \
                       '<span style="font-size: 0.9rem; font-weight: 600;">{status_text}</span>' \
                       '</li>'.format(border_color=border_color, problem_name=problem.get('name', 'Unknown'), status_text=status_text)
            html += '</ul></div>'
        
        # 添加最近比赛记录
        if user_data.get('contests'):
            html += '<div style="margin-bottom: 20px;">' \
                   '<h4 style="margin: 0 0 12px 0; font-size: 1.1rem; font-weight: 600;">最近比赛</h4>' \
                   '<ul style="list-style: none; padding: 0; margin: 0;">'
            for contest in reversed(user_data['contests']):
                html += '<li style="padding: 8px 12px; margin-bottom: 6px; border-radius: 4px; background-color: #f5f5f5; display: flex; flex-wrap: wrap; gap: 12px; align-items: center;">' \
                       '<span style="font-weight: 500; flex: 1;">{contest_name}</span>' \
                       '<span style="font-size: 0.9rem;">#{rank}</span>' \
                       '<span style="font-size: 0.9rem;">{new_rating} → {old_rating}</span>' \
                       '</li>'.format(
                             contest_name=contest.get('contestName', 'Unknown'),
                             rank=contest.get('rank', 'N/A'),
                             new_rating=contest.get('newRating', 'N/A'),
                             old_rating=contest.get('oldRating', 'N/A')
                         )
            html += '</ul></div>'
        
        # 添加Codeforces链接
        html += '<div style="text-align: center; margin-top: 20px; padding-top: 16px; border-top: 1px solid #e0e0e0;">' \
               '<a href="https://codeforces.com/profile/{handle}" target="_blank" style="color: #1976d2; text-decoration: none; font-weight: 500;">' \
               '查看完整个人主页 →' \
               '</a>' \
               '</div>' \
               '</div>' \
               '</div>'.format(handle=user_data.get('handle', ''))
        
        return html
    
    def _cleanup_cache(self):
        """清理过期的缓存文件"""
        try:
            for filename in os.listdir(self.cache_dir):
                file_path = os.path.join(self.cache_dir, filename)
                if time.time() - os.path.getmtime(file_path) > self.config['cache_ttl'] * 2:
                    os.remove(file_path)
        except Exception as e:
            print(f"清理缓存时出错: {e}")
# mkdocs-codeforces-plugin

一个 MkDocs 插件，用于在文档网站上以美观的卡片形式展示 Codeforces 用户的统计信息。

## 功能特点

- 显示用户的用户名、等级、积分等基本信息
- 展示最近的提交记录及其状态
- 展示最近参加的比赛及积分变化
- 可自定义卡片宽度和主题（浅色/深色）
- 内置缓存系统，避免频繁调用 API
- 响应式设计，适配各种设备屏幕

## 安装方式

使用 pip 安装插件：

```bash
pip install -e plugins/mkdocs_codeforces_plugin
```

或者将其添加到你的 `requirements.txt` 文件中：

```
-e plugins/mkdocs_codeforces_plugin
```

## 配置说明

在你的 `mkdocs.yml` 文件中添加插件配置：

```yaml
plugins:
  - codeforces:
      cache_dir: '.cache/codeforces'  # 缓存目录
      cache_ttl: 3600                 # 缓存有效期（秒）
      default_username: ''            # 默认 Codeforces 用户名
      default_width: '100%'           # 默认卡片宽度
      default_theme: 'light'          # 默认主题（'light' 或 'dark'）
```

别忘了在 `extra_css` 部分添加 CSS 文件：

```yaml
extra_css:
  - https://cdn.jsdelivr.net/npm/lxgw-wenkai-webfont@1.1.0/style.css
  - https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css
  - css/extra.css    # Customazation css
  - css/customize.css # 搜索圆角
  - css/mouse_color.css
  - css/mouse_pattern_svg.css
  - plugins/mkdocs_codeforces_plugin/codeforces.css  # 添加这一行
```

## 使用方法

在你的 Markdown 文件中，使用 `codeforces` 标签来显示用户的统计信息：

```markdown
{% codeforces username="你的_codeforces用户名" width="80%" theme="light" %}
```

参数说明：
- `username`: Codeforces 用户名（必需）
- `width`: 卡片宽度（可选，默认为配置中的值）
- `theme`: 卡片主题，'light' 或 'dark'（可选，默认为配置中的值）

### 示例

```markdown
# 我的 Codeforces 个人资料

这是我的 Codeforces 个人资料：

{% codeforces username="Eurekaimer" width="100%" theme="light" %}
```

## 缓存管理

插件会缓存 API 响应以减少对 Codeforces 的请求次数。你可以：
- 通过 `cache_ttl` 调整缓存持续时间
- 通过删除 `cache_dir` 中的文件手动清除缓存
- 插件会在每次构建后自动清理过期的缓存文件

## 许可证

本项目采用 MIT 许可证 - 详见 LICENSE 文件。
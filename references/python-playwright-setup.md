# Python Playwright Setup（服务器环境）

## 概述
除了 Node.js Playwright 外，服务器上也有 Python Playwright 可用。适合需要 Python 生态（如 pandas 处理数据、requests 配合）的自动化场景。

## 安装与路径

### ⚠️ 关键陷阱：venv vs 系统 Python
Hermes Agent 的 venv (`~/.hermes/hermes-agent/venv/`) **没有** Playwright，且 `pip install` 会因 PEP 668 失败。

**正确方式：用系统 Python**
```bash
# 安装（仅首次）
pip install playwright --break-system-packages -q

# 运行脚本必须用系统 Python
/usr/bin/python3 script.py
```

**错误方式（会失败）：**
```bash
python3 -c "import playwright"  # ← 指向 hermes venv，没有 playwright
pip install playwright           # ← PEP 668 拒绝安装
```

## 可用浏览器

| 浏览器 | 路径 | 备注 |
|--------|------|------|
| Chromium | `/usr/bin/chromium-browser` | ✅ 推荐，无需额外安装 |
| Chrome | `/usr/bin/google-chrome` | ✅ 可用 |
| Edge | `/usr/bin/microsoft-edge` | ✅ 可用（Node.js 脚本默认用这个） |

## 启动参数

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=True,
        executable_path="/usr/bin/chromium-browser",
        args=['--no-sandbox', '--disable-gpu', '--disable-dev-shm-usage']
    )
```

### 参数说明
| 参数 | 作用 |
|------|------|
| `--no-sandbox` | 服务器环境必需（root/容器） |
| `--disable-gpu` | 无 GPU 环境避免报错 |
| `--disable-dev-shm-usage` | 内存不足时防止 /dev/shm 溢出 |

## 页面加载策略

### JS 重型站点（SPA、Dashboard）
```python
# ✅ 推荐：domcontentloaded + 手动等待
page.goto(url, timeout=60000, wait_until="domcontentloaded")
page.wait_for_timeout(5000)

# ❌ 不推荐：networkidle 对 SPA 可能永远不触发
page.goto(url, wait_until="networkidle")  # 可能超时
```

### 轻型页面
```python
page.goto(url, timeout=30000)  # 默认 wait_until="load"
```

## 截图与内容提取
```python
# 截图
page.screenshot(path="/tmp/screenshot.png", full_page=True)

# 获取页面文本（截取前 3000 字符避免过长）
text = page.inner_text("body")[:3000]

# 获取 URL 和标题
print(f"URL: {page.url}")
print(f"Title: {page.title()}")
```

## ⚠️ OAuth 登录流程无法自动化

当目标网站使用 OAuth（如 GitHub、Google 登录）时，无法在无头浏览器中完成：
- 点击 "Continue with GitHub" 会跳转到 github.com 的授权页面
- 需要用户**亲自在浏览器中**登录 GitHub 并授权
- 无头浏览器没有用户的 GitHub session，无法完成授权

**应对方案：**
1. 让用户在自己的浏览器登录后，手动提供 API Key / Cookie
2. 如果网站支持 API Token 直接认证，跳过 OAuth 流程
3. 用 `browser_console` 或 `web_extract` 尝试直接获取数据

## 与 Node.js Playwright 的区别

| 特性 | Python (`/usr/bin/python3`) | Node.js (`node`) |
|------|---------------------------|-------------------|
| 模块路径 | 系统 pip 安装 | `~/.hermes/hermes-agent/node_modules/` |
| 启动命令 | `python3 script.py` | `cd hermes-agent && node script.js` |
| 默认浏览器 | 需指定 `executable_path` | Edge |
| 适用场景 | 数据处理配合、requests 集成 | 前端工具链、JS 生态 |

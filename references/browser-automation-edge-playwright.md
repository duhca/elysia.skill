# 浏览器自动化：Edge + Playwright

## 场景
当需要访问 SPA（单页应用）网站时，curl 无法获取 JavaScript 渲染的内容，需要使用真实浏览器。也适用于被 Cloudflare 保护的站点（如 Fandom Wiki）。

**用户偏好：搜索信息/图片时优先用浏览器，不要用 curl/web_search API。**

## 基础用法：Playwright + Edge
```javascript
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ 
    headless: true,
    executablePath: '/usr/bin/microsoft-edge'
  });
  const page = await browser.newPage();
  
  await page.goto('https://example.com', { 
    waitUntil: 'networkidle',
    timeout: 30000 
  });
  
  await page.waitForTimeout(5000);
  
  const content = await page.evaluate(() => document.body.innerText);
  console.log(content);
  
  await page.screenshot({ path: '/tmp/screenshot.png', fullPage: false });
  
  await browser.close();
})();
```

## 图片搜索工作流（2026-05 验证可用）

### Bing 图片搜索
```javascript
await page.goto('https://www.bing.com/images/search?q=崩坏3+爱莉希雅+高清壁纸');
await page.waitForTimeout(5000);
const images = await page.evaluate(() => {
  const imgs = document.querySelectorAll('img.mimg');
  return Array.from(imgs).slice(0, 10).map(img => img.src).filter(src => src && src.startsWith('http'));
});
```
- 搜索结果图片通常较小（缩略图），需要点进详情页获取大图
- 搜索结果质量一般，可能混入其他游戏/角色的图片

### 百度图片搜索（推荐）
```javascript
await page.goto('https://image.baidu.com/search/index?tn=baiduimage&word=崩坏3+爱莉希雅+高清壁纸');
await page.waitForTimeout(8000);  // 百度加载较慢
const images = await page.evaluate(() => {
  const imgs = document.querySelectorAll('img');
  return Array.from(imgs).map(img => ({
    src: img.src,
    alt: img.alt || '',
    width: img.width,
    height: img.height
  })).filter(item => item.src && item.src.startsWith('http') && item.width > 100);
});
```
- 百度图片搜索结果更丰富，alt 标签包含描述信息
- 可以通过 alt 文本过滤相关图片：`.filter(item => item.alt.includes('爱莉希雅'))`
- 图片 URL 格式：`https://img0.baidu.com/it/u=...&fm=253&fmt=auto&app=138&f=JPEG?w=800&h=1067`

### 下载图片
```javascript
const https = require('https');
const fs = require('fs');

const file = fs.createWriteStream('/tmp/image.jpg');
https.get(url, (response) => {
  response.pipe(file);
  file.on('finish', () => { file.close(); console.log('Saved'); });
}).on('error', (err) => {
  fs.unlink('/tmp/image.jpg');
  console.error('Error: ' + err.message);
});
```

## 进阶：绕过 Cloudflare 反爬检测（2026-05 验证可用）

Fandom Wiki、部分游戏Wiki等站点使用 Cloudflare Bot Detection。普通 headless 浏览器会被拦截（显示 "Just a moment..."）。以下反检测配置经实测可绕过：

```javascript
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ 
    headless: true,
    executablePath: '/usr/bin/microsoft-edge',
    args: [
      '--no-sandbox',
      '--disable-blink-features=AutomationControlled',
      '--disable-features=IsolateOrigins,site-per-process',
    ]
  });
  
  const context = await browser.newContext({
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    viewport: { width: 1920, height: 1080 },
    locale: 'zh-CN',
  });
  
  const page = await context.newPage();
  
  await page.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => false });
  });

  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 30000 });
  
  for (let i = 0; i < 6; i++) {
    await page.waitForTimeout(3000);
    const title = await page.title();
    if (!title.includes('Just a moment') && !title.includes('Cloudflare')) {
      break;
    }
  }
  
  await browser.close();
})();
```

### 反检测要点
| 技术 | 作用 |
|------|------|
| `--disable-blink-features=AutomationControlled` | 移除 Chrome/Edge 的 `window.cdc_` 自动化标记 |
| `Object.defineProperty(navigator,'webdriver',{get:()=>false})` | 隐藏 WebDriver 属性 |
| 自定义 userAgent + viewport | 模拟真实桌面浏览器 |
| 独立 `browser.newContext()` | 隔离指纹，避免默认 context 携带自动化痕迹 |

## 站点兼容性（2026-05 验证）

### 可用站点
- `bing.com/images` — 图片搜索 ✅
- `image.baidu.com` — 百度图片搜索 ✅（推荐，结果更丰富）
- `honkaiimpact3.fandom.com` — Cloudflare 反检测可绕过 ✅
- `miyoushe.com` — 米游社，可访问 ✅（但搜索结果可能不准确）

### 被拦截的站点
- `wiki.biligame.com` — 被腾讯云 EdgeOne 安全策略拦截 ❌（返回 "Restricted Access"）
- `r.jina.ai` — 国内完全不可达 ❌

## NODE_PATH 问题（Node.js）

Hermes Agent 自带 Playwright，但脚本不在 hermes-agent 目录下运行时会找不到模块。解决方案：

```bash
# 方法1：在 hermes-agent 目录下运行
cd /home/ubuntu/.hermes/hermes-agent && node script.js

# 方法2：设置 NODE_PATH
NODE_PATH=/home/ubuntu/.hermes/hermes-agent/node_modules node script.js
```

## Python Playwright 环境

详见 `references/python-playwright-setup.md`，包含：
- 系统 Python 路径（`/usr/bin/python3`）与 venv 陷阱
- Chromium 启动参数（`--no-sandbox`, `--disable-gpu`, `--disable-dev-shm-usage`）
- `domcontentloaded` vs `networkidle` 加载策略选择
- OAuth 登录流程的自动化限制

## 已知陷阱

1. **图片内容验证**：下载图片后务必用 `vision_analyze` 或检查文件大小/尺寸确认内容正确。搜索结果可能混入其他游戏角色的图片（如搜崩坏3爱莉希雅可能得到崩坏2的头像）
2. **缩略图 vs 大图**：Bing 搜索结果通常是缩略图（~300px），需要进入详情页才能获取大图
3. **百度加载时间**：百度图片搜索需要 8 秒以上等待，比 Bing 慢
4. **文件格式**：下载的图片可能是 WebP 格式，需要用 `file` 命令检查实际格式
5. **米游社搜索不准**：米游社搜索关键词可能返回不相关的内容（如搜爱莉希雅返回崩坏2头像）
6. **OAuth 登录不可自动化**：GitHub/Google 等 OAuth 登录需要用户在真实浏览器中交互授权，无头浏览器无法完成。遇到需要 OAuth 登录的网站（如 Zep Cloud），应让用户自己登录后提供 API Key，或寻找替代的 API Token 认证方式

## 注意事项
1. **executablePath**：Edge 路径为 `/usr/bin/microsoft-edge`（已验证可用）
2. **headless 模式**：服务器环境必须使用 headless 模式
3. **等待时间**：Cloudflare challenge 需要 3-15 秒；SPA 页面需要 5 秒以上；百度需要 8 秒+
4. **内容截断**：`page.evaluate()` 返回的文本可能很长（10万+字符），按需用 `substring()` 截取

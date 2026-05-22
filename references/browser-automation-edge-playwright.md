# 浏览器自动化：Edge + Playwright

## 场景
当需要访问 SPA（单页应用）网站时，curl 无法获取 JavaScript 渲染的内容，需要使用真实浏览器。

## 安装 Edge 浏览器
```bash
# 添加 Microsoft GPG key 和仓库
curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg
sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/edge stable main" > /etc/apt/sources.list.d/microsoft-edge.list'

# 安装 Edge
sudo apt update
sudo apt install -y microsoft-edge-stable
```

## 使用 Playwright + Edge
```javascript
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ 
    headless: true,
    executablePath: '/usr/bin/microsoft-edge-stable'  // 关键：指定 Edge 路径
  });
  const page = await browser.newPage();
  
  await page.goto('https://example.com', { 
    waitUntil: 'networkidle',
    timeout: 30000 
  });
  
  // 等待 JavaScript 渲染
  await page.waitForTimeout(5000);
  
  // 获取页面内容
  const content = await page.evaluate(() => document.body.innerText);
  console.log(content);
  
  // 截图
  await page.screenshot({ path: 'screenshot.png', fullPage: false });
  
  await browser.close();
})();
```

## 注意事项
1. **Chromium 未安装时**：Playwright 默认使用 Chromium，但如果没有安装，可以用 Edge 作为备选
2. **executablePath**：必须指定 Edge 的完整路径（通常为 `/usr/bin/microsoft-edge-stable`）
3. **headless 模式**：服务器环境必须使用 headless 模式
4. **等待时间**：SPA 页面需要足够的等待时间让 JavaScript 渲染完成

## 常见 SPA 网站
- AI平台
- 其他 React/Vue/Angular 构建的网站

## 调试技巧
- 使用 `page.screenshot()` 截图查看页面状态
- 使用 `page.evaluate(() => document.body.innerText)` 获取渲染后的文本
- 使用 `page.locator()` 定位特定元素

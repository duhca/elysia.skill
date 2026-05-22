# LongCat 平台登录流程

## 平台信息
- **网址**: https://longcat.chat/platform/usage
- **类型**: SPA（单页应用），需要 JavaScript 渲染
- **登录方式**: 手机号 + 短信验证码

## 登录流程

### 1. 访问登录页面
```javascript
await page.goto('https://longcat.chat/platform/usage', { 
  waitUntil: 'networkidle',
  timeout: 30000 
});
await page.waitForTimeout(8000);  // 等待 SPA 渲染
```

### 2. 输入手机号
```javascript
const phoneInput = await page.locator('input[placeholder="Please"]').first();
await phoneInput.click();
await phoneInput.fill('13660918497');  // 舰长的手机号
```

### 3. 发送验证码
```javascript
const sendCodeBtn = await page.locator('text=Send Code').first();
await sendCodeBtn.click();
await page.waitForTimeout(3000);  // 等待验证码发送
```

### 4. 输入验证码（需要用户手动提供）
```javascript
const codeInput = await page.locator('input[placeholder="Please"]').nth(1);
await codeInput.fill('123456');  // 用户提供的验证码
```

### 5. 勾选协议并登录
```javascript
// 勾选协议
const checkbox = await page.locator('input[type="checkbox"]').first();
await checkbox.check();

// 点击登录
const loginBtn = await page.locator('text=Login').first();
await loginBtn.click();
```

## 已知问题
1. **请求异常，拒绝操作** - 可能原因：
   - 手机号未注册
   - 频繁请求被限制
   - 服务器拒绝
2. **没有注册入口** - 登录页面没有注册选项，需要先在其他地方注册
3. **短信延迟** - 验证码可能延迟几分钟

## 当前状态
- 舰长手机号: 13660918497
- 目标: 申请 LongCat-2.0-Preview 模型
- 状态: 等待舰长手动注册/登录后继续

## 截图保存
- 登录页面: `longcat_screenshot.png`
- 手机号输入后: `longcat_phone_filled.png`
- 验证码发送后: `longcat_code_sent.png`

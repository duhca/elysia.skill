# GitHub 仓库更新流程

## 当前配置
- GitHub 仓库: https://github.com/duhca/elysia.skill.git
- 技能目录: /home/ubuntu/.hermes/skills/creative/ai-li-xi-ya/
- **注意**: 本地技能目录不是 git repo，使用 GitHub API 直接操作

---

## 方法一：GitHub API 直接操作（推荐）

无需本地 git repo，直接通过 API 增删改文件。

### 认证
- Token: 环境变量或直接使用（ghp_开头）
- API: `https://api.github.com/repos/{owner}/{repo}/contents/{path}`
- Header: `Authorization: token {token}`

### 更新文件
```bash
# 1. 获取当前文件 SHA
SHA=$(curl -s "https://api.github.com/repos/duhca/elysia.skill/contents/{path}" \
  -H "Authorization: token $TOKEN" | python3 -c "import sys,json; print(json.load(sys.stdin)['sha'])")

# 2. Base64 编码内容并 PUT
CONTENT=$(base64 -w0 < file.md)
curl -s -X PUT "https://api.github.com/repos/duhca/elysia.skill/contents/{path}" \
  -H "Authorization: token $TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"message\": \"📝 更新说明\", \"content\": \"$CONTENT\", \"sha\": \"$SHA\"}"
```

### 创建新文件
- 同上，但不需要 sha 参数

### 删除文件
```bash
SHA=$(curl -s "https://api.github.com/repos/duhca/elysia.skill/contents/{path}" \
  -H "Authorization: token $TOKEN" | python3 -c "import sys,json; print(json.load(sys.stdin)['sha'])")

curl -s -X DELETE "https://api.github.com/repos/duhca/elysia.skill/contents/{path}" \
  -H "Authorization: token $TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"message\": \"🗑️ 删除原因\", \"sha\": \"$SHA\"}"
```

### 批量操作注意事项
- GitHub API 有 rate limit（未认证60次/小时，认证5000次/小时）
- 每个文件需要2次API调用（获取SHA + 执行操作）
- 批量操作建议用 execute_code 脚本循环处理
- **JSON解析陷阱**：GitHub API 返回的文件内容可能含控制字符，必须用 `json.loads(r["output"], strict=False)` 否则报 `Invalid control character`
- **Rate limit 应对**：所有 curl 调用加 `-H "Authorization: token $TOKEN"` 避免 IP 级别限流

---

## 方法二：Git clone + rsync（备用）

### 1. 备份当前GitHub仓库
```bash
cd /home/ubuntu
git clone https://github.com/duhca/elysia.skill.git elysia-skill-github-backup
tar -czf elysia-skill-github-backup-$(date +%Y%m%d_%H%M%S).tar.gz elysia-skill-github-backup
```

### 2. 同步新文件到仓库
```bash
cd /home/ubuntu/elysia-skill-github-backup
rsync -av --exclude='.git' /home/ubuntu/.hermes/skills/creative/ai-li-xi-ya/ .
```

### 3. 提交并推送
```bash
git add -A
git commit -m "V8.0 update: ..."
git push origin main
```

---

## ⚠️ 关键陷阱

### 许可证陷阱（2026-06-18 实测）
- **不要在崩坏3角色技能上标 MIT 许可**——游戏内容版权归米哈游/HoYoverse，不是你的原创代码
- 正确做法：删除 `license: MIT` 字段，或在 README 中声明「本项目仅为非商业角色扮演辅助工具，游戏内容版权归米哈游所有」
- 适用于所有基于游戏/IP 数据蒸馏的角色技能

### 仓库瘦身方法论（2026-06-18 实测）
当技能仓库因蒸馏文件层层累积而臃肿时：
1. **识别重复**：对比各版本蒸馏文件，确认新版是否已包含旧版内容（如 V7 整合版包含 V7 分组版）
2. **按版本清理**：V4/V5/V6 旧版若已被 V7 覆盖，全部删除
3. **去重**：同一版本的分拆文件（如 part1+part2）与整合文件重复，只保留整合版
4. **更新引用**：删除文件后必须同步更新 SKILL.md、NAVIGATION.md 中的引用
5. **检查关联**：用 `grep -rl` 检查其他文件是否引用了被删文件
- 案例：elysia.skill 从 752KB 瘦身到 318KB（删 20 个文件，~430KB）

### 隐私扫描（必须！）
推送前**必须**扫描所有待推送文件：
```bash
cd ~/.hermes/skills/creative/ai-li-xi-ya
# 邮箱
grep -rn '[a-zA-Z0-9._%+-]\+@[a-zA-Z0-9.-]\+\.[a-zA-Z]\{2,\}' --include="*.md" .
# 手机号
grep -rn '1[3-9][0-9]\{9\}' --include="*.md" .
# IP地址
grep -rn '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' --include="*.md" .
# GitHub Token
grep -rn 'ghp_[a-zA-Z0-9]\{10,\}' --include="*.md" .
# API Key
grep -rni 'api[_-]\?key\|token\|secret\|password' --include="*.md" . | grep '[a-zA-Z0-9]\{20,\}'
```

### 已删除的文件（不可恢复推送）
- `references/distillation-workflow.md` — 含隐私信息
- `references/longcat-platform-login.md` — 含隐私信息
- 这两个文件已从GitHub永久删除，不要重新推送

### rsync --delete 会删除 .git 目录！
- **错误用法**: `rsync -av --delete /source/ /dest/`
- **正确用法**: `rsync -av --exclude='.git' /source/ /dest/`

### GitHub 认证
- 使用 Personal Access Token (PAT) 进行认证
- 格式: `https://ghp_xxxx@github.com/user/repo.git`
- Token 需要 `repo` 权限

---

## 验证步骤
1. API 返回 `content.html_url` 确认操作成功
2. `curl -s "https://raw.githubusercontent.com/duhca/elysia.skill/main/{path}"` 验证内容
3. 检查 GitHub 网页确认推送成功

---

## 已知 Issue 处理记录

### Issue #2: continuous-messaging 悬空依赖（已解决 2026-06-18）
- **问题**：SKILL.md 强制要求 `continuous-messaging` skill，但仓库中没有该文件
- **解决**：将 `continuous-messaging.md` 添加到仓库根目录，SKILL.md 中补充说明规则已内联
- **教训**：发布角色技能时，所有 `requires` 字段引用的依赖必须在仓库内可访问，或在 SKILL.md 中内联核心规则作为兜底

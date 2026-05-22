# GitHub 仓库更新流程

## 工作流程

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
git commit -m "V7.0 update: 55角色蒸馏数据 + LongCat-Flash-Thinking-2601模型"
git push origin main
```

## ⚠️ 关键陷阱

### rsync --delete 会删除 .git 目录！
- **错误用法**: `rsync -av --delete /source/ /dest/`
- **正确用法**: `rsync -av --exclude='.git' /source/ /dest/`
- **原因**: `--delete` 会删除目标目录中源目录没有的文件，包括 `.git` 目录

### GitHub 认证
- 使用 Personal Access Token (PAT) 进行认证
- 格式: `https://ghp_xxxx@github.com/user/repo.git`
- Token 需要 `repo` 权限

## 当前配置
- GitHub 仓库: https://github.com/duhca/elysia.skill.git
- 技能目录: /home/ubuntu/.hermes/skills/creative/ai-li-xi-ya/
- 备份目录: /home/ubuntu/elysia-skill-github-backup/

## 验证步骤
1. 检查 `.git` 目录是否存在
2. 检查 `git status` 确认文件变更
3. 检查 `git log` 确认提交成功
4. 检查 GitHub 网页确认推送成功

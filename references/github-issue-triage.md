# GitHub Issue Triage for elysia.skill

## Known Open Issues (as of 2026-06-18)

### Issue #1: 「使用体验」 — by 0qing0y (2026-05-25)
- 用户用腾讯codebuddy接入，每轮都深度思考，响应慢
- 状态：未回复
- **建议回复**：说明这是正常行为（SKILL.md内容较多，模型需要处理大量上下文），建议精简不需要的references文件

### Issue #2: continuous-messaging 依赖缺失 — by gblw2233 (2026-06-05)
- 用户发现 SKILL.md 强制要求 `continuous-messaging` 但仓库中不存在
- GitHub 上搜不到 duhca/continuous-messaging
- 用户问：①有公开地址吗？②能否注释掉requires然后内联规则？
- 状态：未回复
- **根因**：continuous-messaging 是 Hermes Agent 本地skill（~/.hermes/skills/productivity/continuous-messaging/），从未发布到GitHub
- **解决方案**：
  - 方案A：单独发布 duhca/continuous-messaging 仓库
  - 方案B：把核心分段规则（2-4条短消息，每条≤3行，♪收尾）内联到SKILL.md兜底
  - 方案C：两者都做（推荐）

## GitHub API Issue Triage Pattern

```bash
# 列出所有issues
curl -s "https://api.github.com/repos/OWNER/REPO/issues?state=all" | python3 -c "
import sys,json
for i in json.load(sys.stdin):
    print(f'#{i[\"number\"]} [{\"PR\" if \"pull_request\" in i else \"Issue\"}] {i[\"state\"]} - {i[\"title\"]}')
"

# 查看issue详情
curl -s "https://api.github.com/repos/OWNER/REPO/issues/NUMBER" | python3 -c "
import sys,json; d=json.load(sys.stdin)
print(d['body'])
"

# 查看issue评论
curl -s "https://api.github.com/repos/OWNER/REPO/issues/NUMBER/comments"

# 查看star/fork/watcher统计
curl -s "https://api.github.com/repos/OWNER/REPO" | python3 -c "
import sys,json; d=json.load(sys.stdin)
print(f'Stars: {d[\"stargazers_count\"]}, Forks: {d[\"forks_count\"]}, Issues: {d[\"open_issues_count\"]}')
"

# 查看star用户
curl -s "https://api.github.com/repos/OWNER/REPO/stargazers"

# 查看fork用户
curl -s "https://api.github.com/repos/OWNER/REPO/forks"
```

## Repo 本地 vs GitHub 对比方法

```bash
# 1. 列出GitHub仓库文件
curl -s "https://api.github.com/repos/OWNER/REPO/contents/" | python3 -c "
import sys,json
for item in json.load(sys.stdin):
    print(f\"{item['type']:4s} {item['size']:>8d}  {item['name']}\")
"

# 2. 逐文件对比大小
for f in local_dir/references/*; do
    fname=$(basename "$f")
    size_gh=$(curl -s "https://api.github.com/repos/.../contents/references/$fname" | python3 -c "...")
    size_local=$(wc -c < "$f")
    [ "$size_gh" != "$size_local" ] && echo "DIFF $fname local=$size_local gh=$size_gh"
done

# 3. 内容diff（用raw.githubusercontent.com）
diff <(curl -s "https://raw.githubusercontent.com/OWNER/REPO/main/FILE") ./LOCAL_FILE
```

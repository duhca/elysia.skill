# elysia.skill 仓库维护计划

> 最后分析：2026-06-18
> 本地大小：752KB | GitHub大小：262KB（API报告，含git压缩）

## 问题：蒸馏文件层层累积

从 V4 到 V7，每一版蒸馏文件都没删，导致 references/ 占 552KB（总量73%）。

## 清理清单

### 第一批：V4/V5/V6 旧蒸馏（V7 全覆盖）— ~184KB

| 文件 | 大小 | 版本 | 原因 |
|------|------|------|------|
| distill-relation-dialogues.md | 34KB | V4 | V7 distill-all-characters-v7.md 已覆盖 |
| distill-emotional-transitions.md | 22KB | V4 | 同上 |
| distill-cultural-context.md | 21KB | V4 | 同上 |
| distill-philosophical-dialogues.md | 12KB | V4 | 同上 |
| distill-philosophical-dialogues-v5.md | 19KB | V5 | 同上 |
| distill-emotional-transitions-v5.md | 11KB | V5 | 同上 |
| distill-cultural-context-v5.md | 10KB | V5 | 同上 |
| distill-relation-dialogues-v5.md | 6KB | V5 | 同上 |
| distill-elysia-relations-v6.md | 16KB | V6 | 同上 |
| distill-other-relations-v6.md | 13KB | V6 | 同上 |

### 第二批：V7 重复文件（all-characters-v7 已包含）— ~124KB

| 文件 | 大小 | 原因 |
|------|------|------|
| distill-v7-part1.md | 36KB | part1+part2 = all-characters-v7 |
| distill-v7-part2.md | 33KB | 同上 |
| distill-elysia-relations-v7.md | 21KB | all-characters-v7 的子集 |
| distill-hi2-relations-v7.md | 12KB | 同上 |
| distill-schiksal-relations-v7.md | 8KB | 同上 |
| distill-protagonist-relations-v7.md | 6KB | 同上 |
| distill-firefly-relations-v7.md | 5KB | 同上 |
| distill-anti-entropy-relations-v7.md | 5KB | 同上 |
| distill-world-serpent-relations-v7.md | 3KB | 同上 |

### 保留

- `distill-all-characters-v7.md` — 70KB（V7整合版，唯一需要的蒸馏文件）
- `distill-relationship-map-v6.md` — 8KB（关系图谱格式，V7里没有这个格式）

### 清理后需同步更新

- `SKILL.md` — 删除对已删文件的引用
- `NAVIGATION.md` — 更新文件列表
- `scripts/nav.py` — 如有硬编码路径需更新

### 预计效果

- references/: 552KB → ~240KB
- 总量: 752KB → ~440KB

## 已完成的维护

- [x] 2026-06-18: 添加 continuous-messaging.md 到仓库（解决 Issue #2 悬空依赖）
- [ ] 蒸馏文件瘦身（待执行）
- [ ] 本地 V8.0 推送到 GitHub（V8 新增：红线#4/#5、导航工具、MiMo验证限制）
- [ ] 回复 Issue #1 和 #2

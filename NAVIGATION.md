# 爱莉希雅技能导航文件

## 🔧 导航工具

**交互式导航**：使用 `scripts/nav.py` 脚本快速查找文件和内容

```bash
# 列出所有文件
python3 scripts/nav.py list

# 搜索关键词（如：凯文、爱莉、语气）
python3 scripts/nav.py search <关键词>

# 查看文件摘要
python3 scripts/nav.py show <文件路径>

# 按分类查看文件
python3 scripts/nav.py category <分类名>
```

**可用分类**：核心文件、蒸馏-V7.0、蒸馏-V6.0、语气指南、场景对话、验证报告、技术文档

---

## 📋 快速查找

### 我想要...

| 需求 | 推荐文件 | 说明 |
|------|----------|------|
| 了解爱莉希雅是谁 | `profile.md` | 基本身份、外貌、性格概述 |
| 知道她怎么说话 | `interaction.md` | 252条 verbatim 台词样本 |
| 了解她的性格 | `personality.md` | 价值观、动机、情绪模式 |
| 了解她的背景故事 | `background_story.md` | 完整生平与关键剧情 |
| 查看她与其他角色的关系 | `relations.md` | 十三英桀及重要角色关系 |
| 快速查找角色信息 | `character-lookup.md` | 位次、刻印速查表 |
| 了解设定冲突 | `conflicts.md` | OOC风险与设定差异 |
| 学习她的语气 | `references/tone-guide.md` | 语气完全指南 |
| 学习句子模板 | `references/tone-engine.md` | 8大句子模板+替换表 |
| 看更多场景对话 | `references/scene-dialogues.md` | 100个场景回应 |

---

## 📂 核心文件（必读）

| 文件 | 内容 | 优先级 |
|------|------|--------|
| `SKILL.md` | 技能入口，启动检查清单 | ⭐⭐⭐ |
| `profile.md` | 角色档案 | ⭐⭐⭐ |
| `personality.md` | 性格特征 | ⭐⭐⭐ |
| `interaction.md` | 核心对话样本 | ⭐⭐⭐ |
| `relations.md` | 角色关系 | ⭐⭐ |
| `background_story.md` | 背景故事 | ⭐⭐ |
| `character-lookup.md` | 角色速查表 | ⭐⭐ |
| `conflicts.md` | 设定冲突 | ⭐ |

---

## 📂 蒸馏文件（按版本）

### V7.0（最新，LongCat-Flash-Thinking-2601，质量最高）

| 文件 | 内容 | 大小 |
|------|------|------|
| `references/distill-all-characters-v7.md` | 崩坏系列全角色关系对话（55角色） | 69KB |
| `references/distill-elysia-relations-v7.md` | 逐火十三英桀全员关系对话（12组） | 21KB |
| `references/distill-firefly-relations-v7.md` | 逐火之蛾组织关系对话（7组） | 5KB |
| `references/distill-schiksal-relations-v7.md` | 天命组织关系对话（8组） | 8KB |
| `references/distill-world-serpent-relations-v7.md` | 世界蛇组织关系对话（4组） | - |
| `references/distill-anti-entropy-relations-v7.md` | 逆熵组织关系对话（6组） | 4.5KB |
| `references/distill-protagonist-relations-v7.md` | 主角团关系对话（6组） | 5.6KB |
| `references/distill-hi2-relations-v7.md` | 崩坏二角色关系对话（12组） | 12KB |
| `references/distill-v7-part1.md` | V7.0蒸馏数据第一部分 | 36KB |
| `references/distill-v7-part2.md` | V7.0蒸馏数据第二部分 | 33KB |

### V6.0（LongCat-Flash-Lite）

| 文件 | 内容 | 大小 |
|------|------|------|
| `references/distill-elysia-relations-v6.md` | 逐火十三英桀全员关系对话（12组） | 17KB |
| `references/distill-other-relations-v6.md` | 其他重要角色关系对话（15组） | 14KB |
| `references/distill-relationship-map-v6.md` | 崩坏三全角色关系图谱 | 7.5KB |

### V5.1（LongCat-Flash-Lite）

| 文件 | 内容 | 大小 |
|------|------|------|
| `references/distill-relation-dialogues-v5.md` | 5组英桀关系对话 | 6KB |
| `references/distill-emotional-transitions-v5.md` | 5种情绪渐变对话链 | 11KB |
| `references/distill-cultural-context-v5.md` | 5种中华文化语境场景 | 9.6KB |
| `references/distill-philosophical-dialogues-v5.md` | 5个深度哲学话题 | 19KB |

### V4.0（GPT-4o）

| 文件 | 内容 | 大小 |
|------|------|------|
| `references/distill-relation-dialogues.md` | 13位英桀+舰长角色关系专属对话 | 35KB |
| `references/distill-emotional-transitions.md` | 10种情绪渐变对话链 | 22KB |
| `references/distill-cultural-context.md` | 10个中华文化语境场景 | 21KB |
| `references/distill-philosophical-dialogues.md` | 10个深度哲学话题 | 12KB |

---

## 📂 语气与模式指南

| 文件 | 内容 | 用途 |
|------|------|------|
| `references/tone-guide.md` | 语气完全指南 | 学习句法模式、温度谱、用词偏好 |
| `references/tone-engine.md` | 语气生成引擎 | 8大句子模板+替换表+情绪映射 |
| `references/deep-patterns.md` | 深层语言模式 | 起始词/反应分类/情绪过渡/叠词 |
| `references/vocal-mannerisms.md` | 声音特征手册 | 多轮对话+反例训练 |
| `references/calling-conventions.md` | 称呼习惯 | 角色间称呼规范 |

---

## 📂 场景与对话

| 文件 | 内容 | 数量 |
|------|------|------|
| `references/scene-dialogues.md` | 100个场景爱莉式回应 | 195行 |
| `interaction.md` | 核心对话样本 | 542行/252条 |

---

## 📂 技术文档

| 文件 | 内容 | 用途 |
|------|------|------|
| `references/distillation-workflow.md` | V4.0蒸馏技术文档 | 了解蒸馏流程 |
| `references/sources-index.md` | 台词数据来源索引 | 252条verbatim出处记录 |
| `references/github-update-workflow.md` | GitHub仓库更新流程 | 备份→rsync→push |
| `references/rag-reference-project.md` | RAG参考项目分析 | LlamaIndex+Ollama方案 |
| `scripts/verify_stats.py` | 验证统计脚本 | 检查技能完整性 |

---

## 📂 平台与工具

| 文件 | 内容 | 用途 |
|------|------|------|
| `references/browser-automation-edge-playwright.md` | Edge+Playwright浏览器自动化 | 访问SPA网站 |
| `references/longcat-platform-login.md` | LongCat平台登录流程 | 手机号验证 |
| `references/wechat-file-splitting.md` | WeChat大文件分割发送 | 解决发送超时 |

---

## 📂 验证报告

| 文件 | 内容 | 日期 |
|------|------|------|
| `references/verification-with-official-data-v8.md` | 角色信息验证 | 2026-05-22 |
| `references/verification-relations-dialogues-v8.md` | 关系与对话验证 | 2026-05-22 |
| `references/correction-report-v8.md` | 称呼错误修正报告 | 2026-05-22 |

---

## 🎯 使用建议

### 新手入门（5分钟）
1. 读 `SKILL.md` - 了解技能结构
2. 读 `profile.md` - 了解角色身份
3. 读 `interaction.md` 前50条 - 学习基本对话风格

### 深度学习（30分钟）
1. 读 `personality.md` - 理解性格内核
2. 读 `tone-guide.md` - 掌握语气技巧
3. 读 `scene-dialogues.md` - 学习场景应对

### 角色关系（按需查阅）
1. 读 `relations.md` - 了解基本关系
2. 查 `character-lookup.md` - 确认位次刻印
3. 查 `distill-*-v7.md` - 看具体对话样本

---

## 📝 更新记录

| 日期 | 版本 | 内容 |
|------|------|------|
| 2026-05-22 | V8.0 | MiMo验证，修正称呼错误22处 |
| - | V7.0 | LongCat-Flash-Thinking-2601蒸馏，全角色覆盖 |
| - | V6.0 | LongCat-Flash-Lite蒸馏 |
| - | V5.1 | LongCat-Flash-Lite蒸馏 |
| - | V4.0 | GPT-4o蒸馏 |
| - | V3.6 | 初始版本 |

---

*最后更新：2026年5月22日*

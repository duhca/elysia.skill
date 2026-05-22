## Enhancement Workflow (MiMo v2.5-pro)

When enhancing the skill with Xiaomi MiMo v2.5-pro:

1. **Backup first** — Always send current version to user's email before making changes
   - Use QQ邮箱 SMTP: sender `3658215648@qq.com`, receiver `3439246536@qq.com`
   - Package as tar.gz, subject: `【备份】爱莉希雅技能 V{version} 完整备份`

2. **Enhancement areas** (prioritized by MiMo's reasoning strengths):
   - 🎭 Deep philosophical dialogues (爱、牺牲、存在)
   - 💖 Emotional transition chains (悲伤→希望, 焦虑→安心)
   - 🔍 Character deep analysis (内在矛盾、价值观冲突)
   - 🎬 New scene dialogues (未覆盖场景)

3. **Quality verification** — Cross-reference with character-lookup.md for accuracy
```
Game Data (wiki/scripts/quotes)
       │
       ▼ web_search + web_extract
  Raw source material (Baidu Baike, NGA, Bilibili, Fandom, Zhihu)
       │
       ▼ Manual curation → interaction.md
  252 verbatim lines across 22 categories
       │
       ▼ GPT-4o Distillation (GitHub Models API)
  Task 1: Relation dialogues (13 characters × 8 exchanges) → 35KB
  Task 2: Emotional transitions (10 emotions × 3-5 rounds) → 22KB
  Task 3: Cultural context (10 Chinese festivals) → 21KB
  Task 4: Philosophical dialogues (10 topics) → 12KB
       │
  Background story expansion: 28KB → 75KB
  5-part segmented generation → merge
       │
       ▼ Merge + Package
  SKILL.md + manifest.json updated → V4.0
```

## Key Techniques

### 1. Multi-API Distillation (Model Priority Order)
- **GPT-4o (GitHub Models)**: Best for nuanced Chinese character dialogue. Free tier: Low (15 RPM, 150 RPD). Use ONLY when LongCat output quality is insufficient for a specific task.

**Important: User correction** — "记住要使用龙猫模型，优先使用LongCat-Flash-Lite". Do NOT default to MiMo or GPT-4o without trying LongCat first.

### 2. 分段生成 for Large Documents
When generating documents too large for a single API response:
1. Divide into logical parts (character overview, story, relationships, appendix)
2. Generate each part as a separate API call
3. Add `---` separators between parts
4. Merge into single file
5. Each part ≤ 8192 output tokens

### 3. V4.0 Reference File Structure
New files go under `references/` with `distill-` prefix:
```
references/distill-relation-dialogues.md      # 35KB - 13 character relations
references/distill-emotional-transitions.md   # 22KB - 10 emotional arcs
references/distill-cultural-context.md        # 21KB - 10 Chinese cultural scenes
references/distill-philosophical-dialogues.md # 12KB - 10 philosophical topics
```

### 4. API Endpoints Reference
```yaml
GitHub Models: https://models.inference.ai.azure.com/v1
  Models: gpt-4o, gpt-4o-mini, gpt-4.1, gpt-4.1-mini
  Auth: Bearer github_pat_xxx
  Free: 15 RPM / 150 RPD (Low tier)

  Models: LongCat-Flash-Chat (256K ctx), LongCat-Flash-Thinking
  Auth: Bearer ak_xxx
  Free: 500K tokens/day

  Auth: Bearer tp_xxx
  Status: Paid subscription (tp- prefix key)
```

### 3. Full Character Coverage (V6.0+)

**Requirement: Distill ALL Honkai Impact 3 characters, not just the 13 heroes.**

User explicitly requested: "还要把崩坏三所有角色以及关系蒸馏进去"

#### Character List (27+ characters)

**Core: 逐火十三英桀 (12, excluding Elysia)**
| 位次 | 刻印 | 名字 | 蒸馏要点 |
|------|------|------|---------|
| 1 | 救世 | 凯文·卡斯兰娜 | 冷漠简短、重情义、冰之律者 |
| 3 | 戒律 | 阿波尼亚 | 神秘温柔、命运之眼、修女 |
| 4 | 黄金 | 伊甸 | 优雅歌者、爱莉最好的姐妹 |
| 5 | 螺旋 | 维尔薇 | 多重人格、疯狂发明家 |
| 6 | 鏖灭 | 千劫 | 暴躁但纯粹、被爱莉吃得死死的 |
| 7 | 天慧 | 苏 | 温和稳重医者、爱莉喜欢逗他 |
| 8 | 刹那 | 樱 | 温柔沉默、粉毛尖耳 |
| 9 | 旭光 | 科斯魔 | 温柔内向少年、犄角与六芒星 |
| 10 | 无限 | 梅比乌斯 | 毒舌傲娇、疯狂科学家 |
| 11 | 繁星 | 格蕾修 | 喜欢画画的小女孩 |
| 12 | 浮生 | 华 | 认真努力后辈、后来的识之律者 |
| 13 | 空梦 | 帕朵菲莉丝 | 猫耳娘、爱莉最喜欢的妹妹 |

**Extended: Other Important Characters (15)**
| 角色 | 身份 | 蒸馏要点 |
|------|------|---------|
| 雷电芽衣 | 继任者/真红骑士 | 爱莉的传承者、温柔坚强 |
| 克莱茵 | 梅比乌斯助手 | 聪明可爱、忠于梅比乌斯 |
| 布兰卡 | 格蕾修母亲 | 温柔贤惠 |
| 痕 | 格蕾修父亲 | 英勇战士 |
| 梅博士 | 首席科学家 | 理性领袖、凯文搭档 |
| 奥托·阿波卡利斯 | 天命主教 | 复杂角色、对卡莲有执念 |
| 卡莲·卡斯兰娜 | 天命圣女 | 凯文妹妹、温柔善良 |
| 德丽莎·阿波卡利斯 | 学园长 | 奥托侄女、可爱但认真 |
| 琪亚娜·卡斯兰娜 | 空之律者 | K-423、成长型主角 |
| 布洛妮娅·扎伊切克 | 理之律者 | 天才少女、冷静理性 |
| 符华 | 识之律者 | 华的转世、认真严肃 |
| 幽兰黛尔 | S级女武神 | 最强战士之一 |
| 丽塔·洛丝薇瑟 | S级女武神 | 优雅但腹黑 |
| 八重樱 | 巫女 | 樱的转世、温柔沉默 |
| 八重霞 | 樱的妹妹 | 活泼可爱 |

#### Distillation Output Types

1. **Relation Dialogues** — 3-8 dialogue exchanges per character, tagged with interaction type
2. **Emotional Transitions** — 10 emotion arcs (悲伤→希望, 焦虑→安心, etc.)
3. **Cultural Context** — 10 Chinese festival/scene dialogues
4. **Philosophical Dialogues** — 10 philosophical topics
5. **Relationship Map** — 【NEW V6.0】Character relationship graph centered on Elysia, with:
   - Relationship type (战友/知己/冤家/传承 etc.)
   - Intimacy level (普通/亲密/特别亲密)
   - Key interaction quotes

#### V6.0 File Structure
```
references/distill-elysia-relations-v6.md      # 13 heroes relations (12 chars)
references/distill-other-relations-v6.md       # Other characters (15 chars)
references/distill-relationship-map-v6.md      # Full relationship graph
```

### 4. Quality Validation (MANDATORY — NEVER SKIP)

**User correction (2026-05-21): "蒸馏完之后你得先验证是否是正确的"**

**Rule: NEVER report distillation as "完成" until verification passes. This is not optional — user explicitly corrected this workflow.**

**Verification must happen BEFORE reporting completion, not after.**

**Verification methodology:**
1. Load `character-lookup.md` (位次/刻印/性格速查表)
2. Read each generated `distill-*.md` file
3. Check against lookup table:
   - 角色位次和刻印是否正确（例：梅比乌斯是第10位「无限」，不是第3位）
   - 角色性格是否一致（例：凯文冷漠简短，梅比乌斯毒舌傲娇）
   - 对话风格是否符合角色（例：爱莉用♪结尾、花星风月意象）
   - 文化表述是否准确（例：春节/中秋/端午的习俗描述）
4. Report findings: ✅ correct / ⚠️ needs fix / ❌ wrong
5. If issues found → fix before declaring complete
6. If clean → report with verification summary

**Verification checklist template:**
| 维度 | 检查项 | 结果 |
|------|--------|------|
| 角色准确性 | 位次、刻印、身份 | ✅/⚠️/❌ |
| 性格一致性 | 说话风格、口头禅、语气 | ✅/⚠️/❌ |
| 对话自然度 | ♪使用、语气词、意象 | ✅/⚠️/❌ |
| 文化准确性 | 节日习俗、诗词引用 | ✅/⚠️/❌ |
| 哲学深度 | 符合角色世界观 | ✅/⚠️/❌ |

**Other validation rules:**
- Test generated dialogues with multiple models before integration
- Check for tone fidelity: ♪ endings, ～ softeners, 花/星/风 imagery
- Cross-reference lore accuracy against game sources
- Score honestly — the user hates inflated quality scores

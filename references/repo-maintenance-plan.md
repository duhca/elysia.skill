# elysia.skill 仓库维护记录

> 最后更新：2026-06-18

## 已完成的维护

### 2026-06-18 瘦身 + V8.0 同步

**清理内容：**
- 删除 V4/V5/V6 旧蒸馏文件（10个，~184KB）
- 删除 V7 重复文件（9个，~124KB）
- 删除含隐私信息的文件（2个：distillation-workflow, longcat-platform-login）
- 移除 SKILL.md 中的 MIT 许可（崩坏3版权归米哈游）
- 添加 continuous-messaging.md 到仓库（解决 Issue #2）
- 更新 SKILL.md / NAVIGATION.md / README.md 到 V8.0

**清理效果：**
- references/: 39个文件/552KB → 19个文件/161KB
- 总量: ~752KB → ~318KB

### 当前仓库结构

- `distill-all-characters-v7.md` — 70KB，唯一的蒸馏整合文件（55角色）
- `continuous-messaging.md` — 分段发言规则（解决悬空依赖）
- 核心文件：profile / personality / interaction / background_story / relations / memory / conflicts

# WeChat 大文件分割发送

## 问题
WeChat 发送大文件时经常超时（"Timeout context manager should be used inside a task"），需要将大文件分割成小块发送。

## 解决方案

### 1. 按行数分割
```bash
# 分割成 700 行的块
split -l 700 input.md output-part-

# 结果：output-part-aa, output-part-ab, output-part-ac, ...
```

### 2. 合并成两个文件
```bash
# 假设分割成 3 个文件，合并前两个为 part1，最后一个为 part2
cat output-part-aa output-part-ab > part1.md
cat output-part-ac > part2.md
```

### 3. 重命名并清理
```bash
mv output-part-aa part1.md
mv output-part-ab part2.md
rm -f output-part-*
```

## 文件大小建议
- **WeChat 发送限制**：建议单个文件 < 40KB
- **分割策略**：按行数分割比按字节分割更好，避免截断内容
- **命名规范**：`原文件名-part1.md`, `原文件名-part2.md`

## 当前配置
- V7.0 蒸馏文件：1442 行，70KB
- 分割结果：
  - `distill-v7-part1.md` (36KB) - 逐火十三英桀 + 逐火之蛾 + 天命
  - `distill-v7-part2.md` (33KB) - 世界蛇 + 逆熵 + 主角团 + 崩坏二

## 注意事项
1. 分割时注意不要截断 Markdown 标题或代码块
2. 按行数分割可以保证内容完整性
3. 发送前检查文件大小，确保 < 40KB

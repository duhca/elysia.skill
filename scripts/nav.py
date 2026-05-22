#!/usr/bin/env python3
"""
爱莉希雅技能导航工具
提供交互式文件搜索和内容查找功能
"""

import os
import re
from pathlib import Path
from typing import List, Dict

SKILL_DIR = Path(__file__).parent.parent


def list_files() -> List[Dict]:
    """列出所有技能文件"""
    files = []
    for md_file in SKILL_DIR.rglob("*.md"):
        rel_path = md_file.relative_to(SKILL_DIR)
        size = md_file.stat().st_size
        files.append({
            "path": str(rel_path),
            "name": md_file.name,
            "size": size,
            "category": categorize_file(md_file.name)
        })
    return sorted(files, key=lambda x: x["category"])


def categorize_file(filename: str) -> str:
    """根据文件名判断分类"""
    if filename in ["SKILL.md", "README.md", "NAVIGATION.md"]:
        return "入口文件"
    elif filename in ["profile.md", "personality.md", "interaction.md", 
                      "relations.md", "memory.md", "background_story.md",
                      "conflicts.md", "character-lookup.md"]:
        return "核心文件"
    elif "distill" in filename:
        if "v7" in filename:
            return "蒸馏-V7.0"
        elif "v6" in filename:
            return "蒸馏-V6.0"
        elif "v5" in filename:
            return "蒸馏-V5.1"
        else:
            return "蒸馏-V4.0"
    elif "tone" in filename or "pattern" in filename or "mannerism" in filename:
        return "语气指南"
    elif "scene" in filename or "dialogue" in filename:
        return "场景对话"
    elif "verification" in filename or "correction" in filename:
        return "验证报告"
    elif "workflow" in filename or "login" in filename or "automation" in filename:
        return "技术文档"
    else:
        return "其他"


def search_content(keyword: str) -> List[Dict]:
    """搜索文件内容"""
    results = []
    for md_file in SKILL_DIR.rglob("*.md"):
        try:
            with open(md_file, "r", encoding="utf-8") as f:
                content = f.read()
            
            if keyword.lower() in content.lower():
                # 找到包含关键词的行
                lines = content.split("\n")
                matching_lines = []
                for i, line in enumerate(lines, 1):
                    if keyword.lower() in line.lower():
                        matching_lines.append({
                            "line_num": i,
                            "content": line.strip()[:100]
                        })
                
                if matching_lines:
                    results.append({
                        "file": str(md_file.relative_to(SKILL_DIR)),
                        "matches": matching_lines[:5]  # 最多显示5个匹配行
                    })
        except:
            pass
    
    return results


def get_file_summary(filepath: str) -> str:
    """获取文件摘要"""
    full_path = SKILL_DIR / filepath
    if not full_path.exists():
        return f"文件不存在: {filepath}"
    
    try:
        with open(full_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        lines = content.split("\n")
        summary = []
        
        # 提取标题和前几行
        for line in lines[:30]:
            if line.strip():
                summary.append(line)
            if len(summary) >= 15:
                break
        
        return "\n".join(summary)
    except Exception as e:
        return f"读取失败: {e}"


def main():
    """主函数 - 命令行接口"""
    import sys
    
    if len(sys.argv) < 2:
        print("📖 爱莉希雅技能导航工具")
        print("="*40)
        print("用法:")
        print("  python nav.py list          - 列出所有文件")
        print("  python nav.py search <关键词> - 搜索内容")
        print("  python nav.py show <文件路径> - 显示文件摘要")
        print("  python nav.py category <分类> - 按分类查看文件")
        print("\n分类: 核心文件, 蒸馏-V7.0, 蒸馏-V6.0, 语气指南, 场景对话")
        return
    
    action = sys.argv[1]
    
    if action == "list":
        files = list_files()
        print(f"\n📁 共 {len(files)} 个文件\n")
        
        # 按分类显示
        categories = {}
        for f in files:
            cat = f["category"]
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(f)
        
        for cat, cat_files in categories.items():
            print(f"\n【{cat}】")
            for f in cat_files:
                size_kb = f["size"] / 1024
                print(f"  {f['name']:40} {size_kb:6.1f}KB")
    
    elif action == "search":
        if len(sys.argv) < 3:
            print("请提供搜索关键词")
            return
        
        keyword = sys.argv[2]
        results = search_content(keyword)
        
        if not results:
            print(f"未找到包含 '{keyword}' 的内容")
            return
        
        print(f"\n🔍 搜索 '{keyword}' 找到 {len(results)} 个文件:\n")
        for r in results[:10]:
            print(f"📄 {r['file']}")
            for match in r["matches"]:
                print(f"   L{match['line_num']}: {match['content']}")
            print()
    
    elif action == "show":
        if len(sys.argv) < 3:
            print("请提供文件路径")
            return
        
        filepath = sys.argv[2]
        summary = get_file_summary(filepath)
        print(f"\n📄 {filepath} 摘要:\n")
        print(summary)
    
    elif action == "category":
        if len(sys.argv) < 3:
            print("请提供分类名称")
            return
        
        category = sys.argv[2]
        files = list_files()
        cat_files = [f for f in files if f["category"] == category]
        
        if not cat_files:
            print(f"未找到分类 '{category}'")
            print(f"可用分类: {', '.join(set(f['category'] for f in files))}")
            return
        
        print(f"\n【{category}】共 {len(cat_files)} 个文件:\n")
        for f in cat_files:
            size_kb = f["size"] / 1024
            print(f"  {f['name']:40} {size_kb:6.1f}KB")
    
    else:
        print(f"未知操作: {action}")
        print("可用操作: list, search, show, category")


if __name__ == "__main__":
    main()

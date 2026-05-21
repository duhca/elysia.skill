#!/usr/bin/env python3
"""Verify dialogue count and structure of the 爱莉希雅 skill."""
import re, os

skill_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
interaction_file = os.path.join(skill_dir, "interaction.md")

with open(interaction_file) as f:
    content = f.read()

verbatim = len(re.findall(r'`verbatim`', content))
artifact = len(re.findall(r'`artifact`', content))
impression = len(re.findall(r'`impression`', content))
categories = [l.strip() for l in content.split('\n') if l.startswith('## ')]

print(f"爱莉希雅 Skill Stats")
print(f"{'='*30}")
print(f"Verbatim lines:  {verbatim}")
print(f"Artifact lines:  {artifact}")
print(f"Impression:      {impression}")
print(f"Total evidence:  {verbatim + artifact + impression}")
print(f"Evidence ratio:  {verbatim/(verbatim+artifact+impression):.0%}")
print(f"Categories:      {len(categories)}")
for c in categories:
    print(f"  · {c.lstrip('# ')}")

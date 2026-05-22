# RAG 参考项目分析

## 项目信息
- **仓库**: [jtydyb-sha/elysia.skill](https://github.com/jtydyb-sha/elysia.skill)
- **Stars**: 2
- **技术栈**: LlamaIndex + Ollama + DeepSeek
- **用途**: 爱莉希雅技能的 RAG 实现参考

## 架构对比

### 他们的方案
```
data_raw/ → data_clean/ → embedding.py → index/vector_store/ → rag_query.py
```
- **嵌入模型**: Ollama `bge-m3:567m-fp16`（本地）
- **LLM**: DeepSeek `deepseek-chat`
- **向量库**: LlamaIndex VectorStoreIndex
- **数据格式**: JSON（结构化）
- **分块**: SentenceSplitter(chunk_size=512, chunk_overlap=50)

### 我们的方案
```
*.md → cowork-semantic-search → LanceDB → Hermes MCP
```
- **嵌入模型**: sentence-transformers `paraphrase-multilingual-MiniLM-L12-v2`（120MB）
- **向量库**: LanceDB（嵌入式）
- **数据格式**: Markdown（灵活）
- **集成方式**: MCP Server（原生集成 Hermes）

## 他们的优势
1. **完整的 RAG 管线** — 从数据清洗到向量化到查询，流程完整
2. **JSON 数据格式** — 结构化数据，便于管理和扩展
3. **LlamaIndex 框架** — 成熟的 RAG 框架，功能丰富
4. **单例模式** — RAGQueryEngine 单例，避免重复加载
5. **查询结果格式** — 返回 sources 和 similarity scores

## 我们的优势
1. **MCP 集成** — 直接接入 Hermes，无需额外脚本
2. **多格式支持** — txt/md/pdf/docx/pptx/csv
3. **本地化** — 完全离线，不需要 Ollama 服务
4. **轻量级** — 内存占用更小（~300-500MB vs 2GB+）
5. **Token 节省** — 实测节省 ~97% tokens

## 可借鉴的点

### 1. JSON 数据格式
把 background_story.md 转成 JSON，便于结构化查询：
```json
{
  "title": "梅比乌斯",
  "content": "...",
  "metadata": {
    "position": 10,
    "sign": "无限",
    "identity": "无限科学家"
  }
}
```

### 2. 数据清洗流程
```
data_raw/ → data_clean/ → embedding.py → index/vector_store/
```
- 原始数据和清洗后数据分开存储
- 便于版本管理和回溯

### 3. 查询结果格式
```python
{
    "question": question,
    "answer": str(response),
    "sources": [
        {
            "content": node.node.text,
            "score": round(node.score, 4),
            "metadata": {
                "file": node.node.metadata.get('file', 'unknown'),
                "title": node.node.metadata.get('title', '')
            }
        }
    ]
}
```

### 4. 配置文件
统一的 config.json 管理模型配置：
```json
{
  "api_key": "YOUR_API_KEY",
  "embed_model": "bge-m3:567m-fp16",
  "llm_model": "deepseek-chat",
  "persist_dir": "index/vector_store",
  "top_k": 3
}
```

## 实施建议

### 短期（当前）
- 保持现有 cowork-semantic-search 方案
- 优化 Markdown 数据格式（加元数据头）

### 中期（可选）
- 把部分数据转成 JSON 格式
- 添加数据清洗脚本
- 优化查询结果格式

### 长期（探索）
- 考虑 LlamaIndex 集成
- 评估 Ollama 本地嵌入模型
- 实现更复杂的 RAG 管线

## 结论
- 我们的方案更适合当前环境（轻量、MCP 集成）
- 他们的方案更适合复杂场景（完整 RAG 管线）
- 可以借鉴他们的数据格式和查询结果格式
- 保持现有方案，逐步优化

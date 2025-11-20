# RAGOps - Retrieval-Augmented Generation Operations

Production RAG pipeline with document processing, vector storage, and LLM integration.

## 🎯 Overview

- Document ingestion and processing
- Vector databases (Qdrant, Weaviate, Milvus)
- Embedding models
- LLM integration
- RAG orchestration (LangChain, LlamaIndex)
- Monitoring and evaluation

## 📦 Components

| Service | Port | Description |
|---------|------|-------------|
| Qdrant | 6333 | Vector database |
| Weaviate | 8080 | Vector database |
| Milvus | 19530 | Vector database |
| Unstructured API | 8000 | Document processing |
| LiteLLM | 4000 | LLM proxy |
| PostgreSQL | 5432 | Metadata store |

## 🚀 Quick Start

```bash
cd RAGOps
cp .env.example .env
./scripts/start.sh
```

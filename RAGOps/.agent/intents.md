# 📚 Retrieval-Augmented Generation Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Retrieval-Augmented Generation Operations domain.

### Intent 1: Ingest documents

- **Trigger phrases**: "Ingest documents", "I need to ingest documents", "Help me ingest documents"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Ingest documents
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Query vector store

- **Trigger phrases**: "Query vector store", "I need to query vector store", "Help me query vector store"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Query vector store
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Evaluate retrieval quality

- **Trigger phrases**: "Evaluate retrieval quality", "I need to evaluate retrieval quality", "Help me evaluate retrieval quality"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Evaluate retrieval quality
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Optimize chunking

- **Trigger phrases**: "Optimize chunking", "I need to optimize chunking", "Help me optimize chunking"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Optimize chunking
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Manage embeddings

- **Trigger phrases**: "Manage embeddings", "I need to manage embeddings", "Help me manage embeddings"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage embeddings
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Monitor RAG pipeline

- **Trigger phrases**: "Monitor RAG pipeline", "I need to monitor rag pipeline", "Help me monitor rag pipeline"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Monitor RAG pipeline
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```



## Intent Routing

Intents are classified using:
1. **Keyword matching** — domain-specific keyword extraction
2. **Semantic similarity** — embedding-based intent classification
3. **LLM reasoning** — for ambiguous or compound intents

## Fallback Behaviour

If an intent cannot be matched:
1. Agent asks for clarification
2. Suggests the most similar supported intent
3. Escalates to human operator if needed

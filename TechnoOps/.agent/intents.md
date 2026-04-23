# 🔬 Technology Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Technology Operations domain.

### Intent 1: Manage R&D project

- **Trigger phrases**: "Manage R&D project", "I need to manage r&d project", "Help me manage r&d project"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage R&D project
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Track patent

- **Trigger phrases**: "Track patent", "I need to track patent", "Help me track patent"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track patent
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Manage innovation pipeline

- **Trigger phrases**: "Manage innovation pipeline", "I need to manage innovation pipeline", "Help me manage innovation pipeline"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage innovation pipeline
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Transfer technology

- **Trigger phrases**: "Transfer technology", "I need to transfer technology", "Help me transfer technology"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Transfer technology
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Check IP compliance

- **Trigger phrases**: "Check IP compliance", "I need to check ip compliance", "Help me check ip compliance"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check IP compliance
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Scout technology

- **Trigger phrases**: "Scout technology", "I need to scout technology", "Help me scout technology"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Scout technology
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

# 🌏 Trade Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Trade Operations domain.

### Intent 1: Process customs declaration

- **Trigger phrases**: "Process customs declaration", "I need to process customs declaration", "Help me process customs declaration"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Process customs declaration
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Manage trade finance

- **Trigger phrases**: "Manage trade finance", "I need to manage trade finance", "Help me manage trade finance"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage trade finance
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Screen for sanctions

- **Trigger phrases**: "Screen for sanctions", "I need to screen for sanctions", "Help me screen for sanctions"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Screen for sanctions
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Manage trade documents

- **Trigger phrases**: "Manage trade documents", "I need to manage trade documents", "Help me manage trade documents"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage trade documents
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Calculate tariff

- **Trigger phrases**: "Calculate tariff", "I need to calculate tariff", "Help me calculate tariff"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Calculate tariff
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Track supply chain

- **Trigger phrases**: "Track supply chain", "I need to track supply chain", "Help me track supply chain"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track supply chain
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

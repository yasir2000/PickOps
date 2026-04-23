# ⚓ Maritime Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Maritime Operations domain.

### Intent 1: Track vessel

- **Trigger phrases**: "Track vessel", "I need to track vessel", "Help me track vessel"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track vessel
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Manage port operations

- **Trigger phrases**: "Manage port operations", "I need to manage port operations", "Help me manage port operations"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage port operations
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Check cargo manifest

- **Trigger phrases**: "Check cargo manifest", "I need to check cargo manifest", "Help me check cargo manifest"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check cargo manifest
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Ensure compliance

- **Trigger phrases**: "Ensure compliance", "I need to ensure compliance", "Help me ensure compliance"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Ensure compliance
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Manage crew docs

- **Trigger phrases**: "Manage crew docs", "I need to manage crew docs", "Help me manage crew docs"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage crew docs
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Optimize route

- **Trigger phrases**: "Optimize route", "I need to optimize route", "Help me optimize route"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Optimize route
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

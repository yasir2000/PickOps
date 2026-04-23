# 🖥️ IT Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the IT Operations domain.

### Intent 1: Log IT incident

- **Trigger phrases**: "Log IT incident", "I need to log it incident", "Help me log it incident"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Log IT incident
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Monitor infrastructure

- **Trigger phrases**: "Monitor infrastructure", "I need to monitor infrastructure", "Help me monitor infrastructure"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Monitor infrastructure
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Run patch cycle

- **Trigger phrases**: "Run patch cycle", "I need to run patch cycle", "Help me run patch cycle"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Run patch cycle
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Resolve incident

- **Trigger phrases**: "Resolve incident", "I need to resolve incident", "Help me resolve incident"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Resolve incident
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Approve change

- **Trigger phrases**: "Approve change", "I need to approve change", "Help me approve change"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Approve change
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Track IT asset

- **Trigger phrases**: "Track IT asset", "I need to track it asset", "Help me track it asset"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track IT asset
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

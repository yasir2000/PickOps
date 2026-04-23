# 📖 Saga Pattern Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Saga Pattern Operations domain.

### Intent 1: Implement saga pattern

- **Trigger phrases**: "Implement saga pattern", "I need to implement saga pattern", "Help me implement saga pattern"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Implement saga pattern
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Manage compensation

- **Trigger phrases**: "Manage compensation", "I need to manage compensation", "Help me manage compensation"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage compensation
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Choreograph saga

- **Trigger phrases**: "Choreograph saga", "I need to choreograph saga", "Help me choreograph saga"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Choreograph saga
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Track state

- **Trigger phrases**: "Track state", "I need to track state", "Help me track state"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track state
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Implement event sourcing

- **Trigger phrases**: "Implement event sourcing", "I need to implement event sourcing", "Help me implement event sourcing"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Implement event sourcing
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Ensure idempotency

- **Trigger phrases**: "Ensure idempotency", "I need to ensure idempotency", "Help me ensure idempotency"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Ensure idempotency
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

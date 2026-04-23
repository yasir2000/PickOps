# 🐄 Dairy Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Dairy Operations domain.

### Intent 1: Check herd health

- **Trigger phrases**: "Check herd health", "I need to check herd health", "Help me check herd health"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check herd health
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Schedule milking

- **Trigger phrases**: "Schedule milking", "I need to schedule milking", "Help me schedule milking"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Schedule milking
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Log milk quality

- **Trigger phrases**: "Log milk quality", "I need to log milk quality", "Help me log milk quality"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Log milk quality
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Optimize feed plan

- **Trigger phrases**: "Optimize feed plan", "I need to optimize feed plan", "Help me optimize feed plan"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Optimize feed plan
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Track reproduction

- **Trigger phrases**: "Track reproduction", "I need to track reproduction", "Help me track reproduction"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track reproduction
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Alert on cold chain issue

- **Trigger phrases**: "Alert on cold chain issue", "I need to alert on cold chain issue", "Help me alert on cold chain issue"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Alert on cold chain issue
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

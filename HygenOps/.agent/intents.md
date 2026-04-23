# 🧼 Hygiene Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Hygiene Operations domain.

### Intent 1: Schedule sanitation task

- **Trigger phrases**: "Schedule sanitation task", "I need to schedule sanitation task", "Help me schedule sanitation task"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Schedule sanitation task
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Run hygiene audit

- **Trigger phrases**: "Run hygiene audit", "I need to run hygiene audit", "Help me run hygiene audit"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Run hygiene audit
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Check compliance score

- **Trigger phrases**: "Check compliance score", "I need to check compliance score", "Help me check compliance score"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check compliance score
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Order hygiene supplies

- **Trigger phrases**: "Order hygiene supplies", "I need to order hygiene supplies", "Help me order hygiene supplies"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Order hygiene supplies
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Log incident

- **Trigger phrases**: "Log incident", "I need to log incident", "Help me log incident"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Log incident
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Track training

- **Trigger phrases**: "Track training", "I need to track training", "Help me track training"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track training
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

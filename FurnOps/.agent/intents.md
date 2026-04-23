# 🪑 Furniture Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Furniture Operations domain.

### Intent 1: Schedule manufacturing

- **Trigger phrases**: "Schedule manufacturing", "I need to schedule manufacturing", "Help me schedule manufacturing"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Schedule manufacturing
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Manage custom order

- **Trigger phrases**: "Manage custom order", "I need to manage custom order", "Help me manage custom order"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage custom order
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Check inventory

- **Trigger phrases**: "Check inventory", "I need to check inventory", "Help me check inventory"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check inventory
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Run quality inspection

- **Trigger phrases**: "Run quality inspection", "I need to run quality inspection", "Help me run quality inspection"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Run quality inspection
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Track delivery

- **Trigger phrases**: "Track delivery", "I need to track delivery", "Help me track delivery"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track delivery
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Manage supplier

- **Trigger phrases**: "Manage supplier", "I need to manage supplier", "Help me manage supplier"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage supplier
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

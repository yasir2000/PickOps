# 💵 Money Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Money Operations domain.

### Intent 1: Set budget

- **Trigger phrases**: "Set budget", "I need to set budget", "Help me set budget"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Set budget
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Track expense

- **Trigger phrases**: "Track expense", "I need to track expense", "Help me track expense"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track expense
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Forecast cash flow

- **Trigger phrases**: "Forecast cash flow", "I need to forecast cash flow", "Help me forecast cash flow"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Forecast cash flow
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Process payment

- **Trigger phrases**: "Process payment", "I need to process payment", "Help me process payment"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Process payment
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Prepare tax docs

- **Trigger phrases**: "Prepare tax docs", "I need to prepare tax docs", "Help me prepare tax docs"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Prepare tax docs
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Track investments

- **Trigger phrases**: "Track investments", "I need to track investments", "Help me track investments"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track investments
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

# ⚗️ Chemical Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Chemical Operations domain.

### Intent 1: Check process parameters

- **Trigger phrases**: "Check process parameters", "I need to check process parameters", "Help me check process parameters"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check process parameters
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Alert on safety breach

- **Trigger phrases**: "Alert on safety breach", "I need to alert on safety breach", "Help me alert on safety breach"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Alert on safety breach
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Check chemical stock

- **Trigger phrases**: "Check chemical stock", "I need to check chemical stock", "Help me check chemical stock"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check chemical stock
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Generate EPA report

- **Trigger phrases**: "Generate EPA report", "I need to generate epa report", "Help me generate epa report"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Generate EPA report
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Find MSDS for chemical

- **Trigger phrases**: "Find MSDS for chemical", "I need to find msds for chemical", "Help me find msds for chemical"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Find MSDS for chemical
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Log safety incident

- **Trigger phrases**: "Log safety incident", "I need to log safety incident", "Help me log safety incident"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Log safety incident
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

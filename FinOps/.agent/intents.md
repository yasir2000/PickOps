# 💰 Cloud Financial Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Cloud Financial Operations domain.

### Intent 1: Analyse cloud costs

- **Trigger phrases**: "Analyse cloud costs", "I need to analyse cloud costs", "Help me analyse cloud costs"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Analyse cloud costs
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Set budget threshold

- **Trigger phrases**: "Set budget threshold", "I need to set budget threshold", "Help me set budget threshold"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Set budget threshold
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Generate chargeback report

- **Trigger phrases**: "Generate chargeback report", "I need to generate chargeback report", "Help me generate chargeback report"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Generate chargeback report
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Manage reserved instances

- **Trigger phrases**: "Manage reserved instances", "I need to manage reserved instances", "Help me manage reserved instances"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage reserved instances
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Find idle resources

- **Trigger phrases**: "Find idle resources", "I need to find idle resources", "Help me find idle resources"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Find idle resources
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Forecast cloud spend

- **Trigger phrases**: "Forecast cloud spend", "I need to forecast cloud spend", "Help me forecast cloud spend"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Forecast cloud spend
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

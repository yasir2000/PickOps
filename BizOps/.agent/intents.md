# 💼 Business Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Business Operations domain.

### Intent 1: Update KPI dashboard

- **Trigger phrases**: "Update KPI dashboard", "I need to update kpi dashboard", "Help me update kpi dashboard"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Update KPI dashboard
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Check OKR status

- **Trigger phrases**: "Check OKR status", "I need to check okr status", "Help me check okr status"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check OKR status
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Automate approval workflow

- **Trigger phrases**: "Automate approval workflow", "I need to automate approval workflow", "Help me automate approval workflow"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Automate approval workflow
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Analyse revenue trend

- **Trigger phrases**: "Analyse revenue trend", "I need to analyse revenue trend", "Help me analyse revenue trend"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Analyse revenue trend
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Generate board report

- **Trigger phrases**: "Generate board report", "I need to generate board report", "Help me generate board report"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Generate board report
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Forecast next quarter

- **Trigger phrases**: "Forecast next quarter", "I need to forecast next quarter", "Help me forecast next quarter"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Forecast next quarter
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

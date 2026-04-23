# 🏘️ Real Estate Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Real Estate Operations domain.

### Intent 1: Manage property portfolio

- **Trigger phrases**: "Manage property portfolio", "I need to manage property portfolio", "Help me manage property portfolio"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage property portfolio
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Create listing

- **Trigger phrases**: "Create listing", "I need to create listing", "Help me create listing"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Create listing
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Handle tenant request

- **Trigger phrases**: "Handle tenant request", "I need to handle tenant request", "Help me handle tenant request"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Handle tenant request
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Manage lease

- **Trigger phrases**: "Manage lease", "I need to manage lease", "Help me manage lease"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage lease
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Analyse investment

- **Trigger phrases**: "Analyse investment", "I need to analyse investment", "Help me analyse investment"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Analyse investment
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Schedule maintenance

- **Trigger phrases**: "Schedule maintenance", "I need to schedule maintenance", "Help me schedule maintenance"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Schedule maintenance
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

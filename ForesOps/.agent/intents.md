# 🌲 Forestry Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Forestry Operations domain.

### Intent 1: Check forest inventory

- **Trigger phrases**: "Check forest inventory", "I need to check forest inventory", "Help me check forest inventory"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check forest inventory
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Plan logging operation

- **Trigger phrases**: "Plan logging operation", "I need to plan logging operation", "Help me plan logging operation"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Plan logging operation
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Track reforestation

- **Trigger phrases**: "Track reforestation", "I need to track reforestation", "Help me track reforestation"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track reforestation
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Monitor fire risk

- **Trigger phrases**: "Monitor fire risk", "I need to monitor fire risk", "Help me monitor fire risk"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Monitor fire risk
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Manage carbon credits

- **Trigger phrases**: "Manage carbon credits", "I need to manage carbon credits", "Help me manage carbon credits"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage carbon credits
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Report compliance

- **Trigger phrases**: "Report compliance", "I need to report compliance", "Help me report compliance"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Report compliance
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

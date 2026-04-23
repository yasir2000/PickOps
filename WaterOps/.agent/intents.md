# 💧 Water Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Water Operations domain.

### Intent 1: Monitor water network

- **Trigger phrases**: "Monitor water network", "I need to monitor water network", "Help me monitor water network"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Monitor water network
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Manage water quality

- **Trigger phrases**: "Manage water quality", "I need to manage water quality", "Help me manage water quality"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage water quality
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Forecast demand

- **Trigger phrases**: "Forecast demand", "I need to forecast demand", "Help me forecast demand"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Forecast demand
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Detect leak

- **Trigger phrases**: "Detect leak", "I need to detect leak", "Help me detect leak"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Detect leak
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Automate treatment

- **Trigger phrases**: "Automate treatment", "I need to automate treatment", "Help me automate treatment"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Automate treatment
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Check compliance

- **Trigger phrases**: "Check compliance", "I need to check compliance", "Help me check compliance"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check compliance
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

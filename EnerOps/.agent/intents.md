# ⚡ Energy Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Energy Operations domain.

### Intent 1: Check grid status

- **Trigger phrases**: "Check grid status", "I need to check grid status", "Help me check grid status"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check grid status
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Dispatch renewable energy

- **Trigger phrases**: "Dispatch renewable energy", "I need to dispatch renewable energy", "Help me dispatch renewable energy"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Dispatch renewable energy
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

### Intent 4: Execute energy trade

- **Trigger phrases**: "Execute energy trade", "I need to execute energy trade", "Help me execute energy trade"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Execute energy trade
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Process meter reading

- **Trigger phrases**: "Process meter reading", "I need to process meter reading", "Help me process meter reading"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Process meter reading
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Track carbon emissions

- **Trigger phrases**: "Track carbon emissions", "I need to track carbon emissions", "Help me track carbon emissions"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track carbon emissions
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

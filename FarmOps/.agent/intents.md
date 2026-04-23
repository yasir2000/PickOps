# 🚜 Farm Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Farm Operations domain.

### Intent 1: Plan crop rotation

- **Trigger phrases**: "Plan crop rotation", "I need to plan crop rotation", "Help me plan crop rotation"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Plan crop rotation
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Track equipment

- **Trigger phrases**: "Track equipment", "I need to track equipment", "Help me track equipment"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track equipment
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Manage supply chain

- **Trigger phrases**: "Manage supply chain", "I need to manage supply chain", "Help me manage supply chain"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage supply chain
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Get weather forecast

- **Trigger phrases**: "Get weather forecast", "I need to get weather forecast", "Help me get weather forecast"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Get weather forecast
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Schedule workers

- **Trigger phrases**: "Schedule workers", "I need to schedule workers", "Help me schedule workers"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Schedule workers
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Generate financial report

- **Trigger phrases**: "Generate financial report", "I need to generate financial report", "Help me generate financial report"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Generate financial report
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

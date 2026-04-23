# 🏭 Manufacturing Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Manufacturing Operations domain.

### Intent 1: Plan production schedule

- **Trigger phrases**: "Plan production schedule", "I need to plan production schedule", "Help me plan production schedule"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Plan production schedule
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Automate QC

- **Trigger phrases**: "Automate QC", "I need to automate qc", "Help me automate qc"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Automate QC
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Integrate MES

- **Trigger phrases**: "Integrate MES", "I need to integrate mes", "Help me integrate mes"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Integrate MES
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Coordinate supply chain

- **Trigger phrases**: "Coordinate supply chain", "I need to coordinate supply chain", "Help me coordinate supply chain"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Coordinate supply chain
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Track OEE

- **Trigger phrases**: "Track OEE", "I need to track oee", "Help me track oee"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track OEE
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Apply lean improvement

- **Trigger phrases**: "Apply lean improvement", "I need to apply lean improvement", "Help me apply lean improvement"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Apply lean improvement
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

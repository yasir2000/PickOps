# 🔨 Construction Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Construction Operations domain.

### Intent 1: Update project schedule

- **Trigger phrases**: "Update project schedule", "I need to update project schedule", "Help me update project schedule"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Update project schedule
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Check site safety status

- **Trigger phrases**: "Check site safety status", "I need to check site safety status", "Help me check site safety status"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check site safety status
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Order materials

- **Trigger phrases**: "Order materials", "I need to order materials", "Help me order materials"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Order materials
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Coordinate subcontractor

- **Trigger phrases**: "Coordinate subcontractor", "I need to coordinate subcontractor", "Help me coordinate subcontractor"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Coordinate subcontractor
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Check budget status

- **Trigger phrases**: "Check budget status", "I need to check budget status", "Help me check budget status"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check budget status
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Log quality inspection

- **Trigger phrases**: "Log quality inspection", "I need to log quality inspection", "Help me log quality inspection"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Log quality inspection
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

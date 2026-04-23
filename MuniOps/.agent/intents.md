# 🏙️ Municipal Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Municipal Operations domain.

### Intent 1: Optimize waste route

- **Trigger phrases**: "Optimize waste route", "I need to optimize waste route", "Help me optimize waste route"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Optimize waste route
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Process utility bill

- **Trigger phrases**: "Process utility bill", "I need to process utility bill", "Help me process utility bill"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Process utility bill
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Apply for permit

- **Trigger phrases**: "Apply for permit", "I need to apply for permit", "Help me apply for permit"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Apply for permit
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Access citizen service

- **Trigger phrases**: "Access citizen service", "I need to access citizen service", "Help me access citizen service"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Access citizen service
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Track municipal asset

- **Trigger phrases**: "Track municipal asset", "I need to track municipal asset", "Help me track municipal asset"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track municipal asset
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Coordinate emergency

- **Trigger phrases**: "Coordinate emergency", "I need to coordinate emergency", "Help me coordinate emergency"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Coordinate emergency
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

# 🚚 Logistics Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Logistics Operations domain.

### Intent 1: Optimize delivery route

- **Trigger phrases**: "Optimize delivery route", "I need to optimize delivery route", "Help me optimize delivery route"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Optimize delivery route
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Manage warehouse

- **Trigger phrases**: "Manage warehouse", "I need to manage warehouse", "Help me manage warehouse"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage warehouse
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Track shipment

- **Trigger phrases**: "Track shipment", "I need to track shipment", "Help me track shipment"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track shipment
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Coordinate last-mile

- **Trigger phrases**: "Coordinate last-mile", "I need to coordinate last-mile", "Help me coordinate last-mile"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Coordinate last-mile
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Process customs

- **Trigger phrases**: "Process customs", "I need to process customs", "Help me process customs"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Process customs
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Monitor cold chain

- **Trigger phrases**: "Monitor cold chain", "I need to monitor cold chain", "Help me monitor cold chain"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Monitor cold chain
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

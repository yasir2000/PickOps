# 🐟 Fishery Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Fishery Operations domain.

### Intent 1: Track vessel location

- **Trigger phrases**: "Track vessel location", "I need to track vessel location", "Help me track vessel location"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track vessel location
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Assess fish stock

- **Trigger phrases**: "Assess fish stock", "I need to assess fish stock", "Help me assess fish stock"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Assess fish stock
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Monitor fish farm

- **Trigger phrases**: "Monitor fish farm", "I need to monitor fish farm", "Help me monitor fish farm"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Monitor fish farm
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Check quota status

- **Trigger phrases**: "Check quota status", "I need to check quota status", "Help me check quota status"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check quota status
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Track cold chain

- **Trigger phrases**: "Track cold chain", "I need to track cold chain", "Help me track cold chain"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track cold chain
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Report sustainability

- **Trigger phrases**: "Report sustainability", "I need to report sustainability", "Help me report sustainability"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Report sustainability
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

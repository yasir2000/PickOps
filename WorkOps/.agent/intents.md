# 🏢 Workplace Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Workplace Operations domain.

### Intent 1: Book desk/room

- **Trigger phrases**: "Book desk/room", "I need to book desk/room", "Help me book desk/room"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Book desk/room
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Manage facilities

- **Trigger phrases**: "Manage facilities", "I need to manage facilities", "Help me manage facilities"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage facilities
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Check in visitor

- **Trigger phrases**: "Check in visitor", "I need to check in visitor", "Help me check in visitor"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check in visitor
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Enhance employee experience

- **Trigger phrases**: "Enhance employee experience", "I need to enhance employee experience", "Help me enhance employee experience"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Enhance employee experience
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Coordinate hybrid work

- **Trigger phrases**: "Coordinate hybrid work", "I need to coordinate hybrid work", "Help me coordinate hybrid work"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Coordinate hybrid work
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Track asset

- **Trigger phrases**: "Track asset", "I need to track asset", "Help me track asset"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track asset
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

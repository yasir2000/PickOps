# 🏛️ Government Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Government Operations domain.

### Intent 1: Deliver digital service

- **Trigger phrases**: "Deliver digital service", "I need to deliver digital service", "Help me deliver digital service"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Deliver digital service
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Manage citizen data

- **Trigger phrases**: "Manage citizen data", "I need to manage citizen data", "Help me manage citizen data"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage citizen data
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Check policy compliance

- **Trigger phrases**: "Check policy compliance", "I need to check policy compliance", "Help me check policy compliance"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check policy compliance
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Coordinate agencies

- **Trigger phrases**: "Coordinate agencies", "I need to coordinate agencies", "Help me coordinate agencies"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Coordinate agencies
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Publish open data

- **Trigger phrases**: "Publish open data", "I need to publish open data", "Help me publish open data"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Publish open data
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Audit government process

- **Trigger phrases**: "Audit government process", "I need to audit government process", "Help me audit government process"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Audit government process
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

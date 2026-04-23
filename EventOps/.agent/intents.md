# 📅 Event Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Event Operations domain.

### Intent 1: Register for event

- **Trigger phrases**: "Register for event", "I need to register for event", "Help me register for event"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Register for event
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Manage ticket allocation

- **Trigger phrases**: "Manage ticket allocation", "I need to manage ticket allocation", "Help me manage ticket allocation"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage ticket allocation
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Coordinate venue

- **Trigger phrases**: "Coordinate venue", "I need to coordinate venue", "Help me coordinate venue"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Coordinate venue
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Manage speaker schedule

- **Trigger phrases**: "Manage speaker schedule", "I need to manage speaker schedule", "Help me manage speaker schedule"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage speaker schedule
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Send event communications

- **Trigger phrases**: "Send event communications", "I need to send event communications", "Help me send event communications"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Send event communications
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Analyse event feedback

- **Trigger phrases**: "Analyse event feedback", "I need to analyse event feedback", "Help me analyse event feedback"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Analyse event feedback
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

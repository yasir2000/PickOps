# 👴 Elder Care Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Elder Care Operations domain.

### Intent 1: Monitor resident health

- **Trigger phrases**: "Monitor resident health", "I need to monitor resident health", "Help me monitor resident health"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Monitor resident health
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Schedule medication

- **Trigger phrases**: "Schedule medication", "I need to schedule medication", "Help me schedule medication"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Schedule medication
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Detect fall event

- **Trigger phrases**: "Detect fall event", "I need to detect fall event", "Help me detect fall event"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Detect fall event
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Notify family

- **Trigger phrases**: "Notify family", "I need to notify family", "Help me notify family"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Notify family
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Update care plan

- **Trigger phrases**: "Update care plan", "I need to update care plan", "Help me update care plan"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Update care plan
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Audit compliance

- **Trigger phrases**: "Audit compliance", "I need to audit compliance", "Help me audit compliance"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Audit compliance
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

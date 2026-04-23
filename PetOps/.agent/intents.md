# 🐾 Pet Care Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Pet Care Operations domain.

### Intent 1: Access pet health record

- **Trigger phrases**: "Access pet health record", "I need to access pet health record", "Help me access pet health record"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Access pet health record
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Schedule vet appointment

- **Trigger phrases**: "Schedule vet appointment", "I need to schedule vet appointment", "Help me schedule vet appointment"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Schedule vet appointment
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Monitor pet health

- **Trigger phrases**: "Monitor pet health", "I need to monitor pet health", "Help me monitor pet health"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Monitor pet health
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Set medication reminder

- **Trigger phrases**: "Set medication reminder", "I need to set medication reminder", "Help me set medication reminder"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Set medication reminder
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Process insurance claim

- **Trigger phrases**: "Process insurance claim", "I need to process insurance claim", "Help me process insurance claim"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Process insurance claim
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Manage breeder info

- **Trigger phrases**: "Manage breeder info", "I need to manage breeder info", "Help me manage breeder info"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage breeder info
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

# 🎯 Service Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Service Operations domain.

### Intent 1: Manage service catalogue

- **Trigger phrases**: "Manage service catalogue", "I need to manage service catalogue", "Help me manage service catalogue"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage service catalogue
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Monitor SLA

- **Trigger phrases**: "Monitor SLA", "I need to monitor sla", "Help me monitor sla"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Monitor SLA
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Automate customer success

- **Trigger phrases**: "Automate customer success", "I need to automate customer success", "Help me automate customer success"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Automate customer success
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Route support ticket

- **Trigger phrases**: "Route support ticket", "I need to route support ticket", "Help me route support ticket"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Route support ticket
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Update knowledge base

- **Trigger phrases**: "Update knowledge base", "I need to update knowledge base", "Help me update knowledge base"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Update knowledge base
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Measure CSAT

- **Trigger phrases**: "Measure CSAT", "I need to measure csat", "Help me measure csat"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Measure CSAT
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

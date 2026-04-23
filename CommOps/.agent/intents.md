# 📡 Communications Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Communications Operations domain.

### Intent 1: Check messaging queue status

- **Trigger phrases**: "Check messaging queue status", "I need to check messaging queue status", "Help me check messaging queue status"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check messaging queue status
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Monitor SIP health

- **Trigger phrases**: "Monitor SIP health", "I need to monitor sip health", "Help me monitor sip health"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Monitor SIP health
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Check email bounce rate

- **Trigger phrases**: "Check email bounce rate", "I need to check email bounce rate", "Help me check email bounce rate"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check email bounce rate
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Route notification campaign

- **Trigger phrases**: "Route notification campaign", "I need to route notification campaign", "Help me route notification campaign"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Route notification campaign
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Archive communications

- **Trigger phrases**: "Archive communications", "I need to archive communications", "Help me archive communications"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Archive communications
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Alert on outage

- **Trigger phrases**: "Alert on outage", "I need to alert on outage", "Help me alert on outage"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Alert on outage
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

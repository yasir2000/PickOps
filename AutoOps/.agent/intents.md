# 🚗 Automotive Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Automotive Operations domain.

### Intent 1: Check fleet status

- **Trigger phrases**: "Check fleet status", "I need to check fleet status", "Help me check fleet status"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check fleet status
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Predict next maintenance

- **Trigger phrases**: "Predict next maintenance", "I need to predict next maintenance", "Help me predict next maintenance"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Predict next maintenance
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Schedule EV charging

- **Trigger phrases**: "Schedule EV charging", "I need to schedule ev charging", "Help me schedule ev charging"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Schedule EV charging
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Optimize delivery route

- **Trigger phrases**: "Optimize delivery route", "I need to optimize delivery route", "Help me optimize delivery route"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Optimize delivery route
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Push software update

- **Trigger phrases**: "Push software update", "I need to push software update", "Help me push software update"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Push software update
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Analyse warranty claims

- **Trigger phrases**: "Analyse warranty claims", "I need to analyse warranty claims", "Help me analyse warranty claims"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Analyse warranty claims
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

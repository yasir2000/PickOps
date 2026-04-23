# 🛍️ Retail Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Retail Operations domain.

### Intent 1: Optimize inventory

- **Trigger phrases**: "Optimize inventory", "I need to optimize inventory", "Help me optimize inventory"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Optimize inventory
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Set pricing

- **Trigger phrases**: "Set pricing", "I need to set pricing", "Help me set pricing"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Set pricing
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Personalize experience

- **Trigger phrases**: "Personalize experience", "I need to personalize experience", "Help me personalize experience"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Personalize experience
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Manage supply chain

- **Trigger phrases**: "Manage supply chain", "I need to manage supply chain", "Help me manage supply chain"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage supply chain
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Coordinate omnichannel

- **Trigger phrases**: "Coordinate omnichannel", "I need to coordinate omnichannel", "Help me coordinate omnichannel"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Coordinate omnichannel
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Process return

- **Trigger phrases**: "Process return", "I need to process return", "Help me process return"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Process return
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

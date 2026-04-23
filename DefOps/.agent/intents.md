# 🛡️ Defence Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Defence Operations domain.

### Intent 1: Secure communication channel

- **Trigger phrases**: "Secure communication channel", "I need to secure communication channel", "Help me secure communication channel"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Secure communication channel
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Plan mission workflow

- **Trigger phrases**: "Plan mission workflow", "I need to plan mission workflow", "Help me plan mission workflow"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Plan mission workflow
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Track supply chain

- **Trigger phrases**: "Track supply chain", "I need to track supply chain", "Help me track supply chain"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track supply chain
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Monitor cyber threats

- **Trigger phrases**: "Monitor cyber threats", "I need to monitor cyber threats", "Help me monitor cyber threats"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Monitor cyber threats
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Process intelligence

- **Trigger phrases**: "Process intelligence", "I need to process intelligence", "Help me process intelligence"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Process intelligence
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Audit ITAR compliance

- **Trigger phrases**: "Audit ITAR compliance", "I need to audit itar compliance", "Help me audit itar compliance"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Audit ITAR compliance
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

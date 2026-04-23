# 🧠 AI for IT Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the AI for IT Operations domain.

### Intent 1: Why is there a spike in errors?

- **Trigger phrases**: "Why is there a spike in errors?", "I need to why is there a spike in errors?", "Help me why is there a spike in errors?"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Why is there a spike in errors?
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Predict next week's capacity needs

- **Trigger phrases**: "Predict next week's capacity needs", "I need to predict next week's capacity needs", "Help me predict next week's capacity needs"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Predict next week's capacity needs
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Correlate alerts from multiple sources

- **Trigger phrases**: "Correlate alerts from multiple sources", "I need to correlate alerts from multiple sources", "Help me correlate alerts from multiple sources"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Correlate alerts from multiple sources
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Auto-remediate high CPU

- **Trigger phrases**: "Auto-remediate high CPU", "I need to auto-remediate high cpu", "Help me auto-remediate high cpu"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Auto-remediate high CPU
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Generate an incident RCA

- **Trigger phrases**: "Generate an incident RCA", "I need to generate an incident rca", "Help me generate an incident rca"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Generate an incident RCA
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Reduce alert noise

- **Trigger phrases**: "Reduce alert noise", "I need to reduce alert noise", "Help me reduce alert noise"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Reduce alert noise
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

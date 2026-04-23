# 🏠 Home Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Home Operations domain.

### Intent 1: Automate home routine

- **Trigger phrases**: "Automate home routine", "I need to automate home routine", "Help me automate home routine"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Automate home routine
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Optimize energy usage

- **Trigger phrases**: "Optimize energy usage", "I need to optimize energy usage", "Help me optimize energy usage"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Optimize energy usage
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Check security feed

- **Trigger phrases**: "Check security feed", "I need to check security feed", "Help me check security feed"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check security feed
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Schedule maintenance

- **Trigger phrases**: "Schedule maintenance", "I need to schedule maintenance", "Help me schedule maintenance"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Schedule maintenance
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Manage smart device

- **Trigger phrases**: "Manage smart device", "I need to manage smart device", "Help me manage smart device"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage smart device
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Integrate voice assistant

- **Trigger phrases**: "Integrate voice assistant", "I need to integrate voice assistant", "Help me integrate voice assistant"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Integrate voice assistant
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

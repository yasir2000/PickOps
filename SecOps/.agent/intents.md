# 🔐 Security Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Security Operations domain.

### Intent 1: Monitor security events

- **Trigger phrases**: "Monitor security events", "I need to monitor security events", "Help me monitor security events"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Monitor security events
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Detect threat

- **Trigger phrases**: "Detect threat", "I need to detect threat", "Help me detect threat"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Detect threat
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Respond to incident

- **Trigger phrases**: "Respond to incident", "I need to respond to incident", "Help me respond to incident"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Respond to incident
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Manage vulnerability

- **Trigger phrases**: "Manage vulnerability", "I need to manage vulnerability", "Help me manage vulnerability"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage vulnerability
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Process threat intel

- **Trigger phrases**: "Process threat intel", "I need to process threat intel", "Help me process threat intel"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Process threat intel
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Orchestrate security tools

- **Trigger phrases**: "Orchestrate security tools", "I need to orchestrate security tools", "Help me orchestrate security tools"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Orchestrate security tools
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

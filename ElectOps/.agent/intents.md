# ⚡ Electronics Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Electronics Operations domain.

### Intent 1: Version PCB design

- **Trigger phrases**: "Version PCB design", "I need to version pcb design", "Help me version pcb design"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Version PCB design
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Run electronics test

- **Trigger phrases**: "Run electronics test", "I need to run electronics test", "Help me run electronics test"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Run electronics test
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Track component status

- **Trigger phrases**: "Track component status", "I need to track component status", "Help me track component status"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track component status
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Check ESD compliance

- **Trigger phrases**: "Check ESD compliance", "I need to check esd compliance", "Help me check esd compliance"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check ESD compliance
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Manage component supply

- **Trigger phrases**: "Manage component supply", "I need to manage component supply", "Help me manage component supply"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage component supply
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Analyse failure mode

- **Trigger phrases**: "Analyse failure mode", "I need to analyse failure mode", "Help me analyse failure mode"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Analyse failure mode
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

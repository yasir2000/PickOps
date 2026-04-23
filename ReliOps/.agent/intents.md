# 🔋 Reliability Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Reliability Operations domain.

### Intent 1: Define SLO

- **Trigger phrases**: "Define SLO", "I need to define slo", "Help me define slo"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Define SLO
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Check error budget

- **Trigger phrases**: "Check error budget", "I need to check error budget", "Help me check error budget"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check error budget
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Run reliability test

- **Trigger phrases**: "Run reliability test", "I need to run reliability test", "Help me run reliability test"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Run reliability test
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Execute chaos experiment

- **Trigger phrases**: "Execute chaos experiment", "I need to execute chaos experiment", "Help me execute chaos experiment"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Execute chaos experiment
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Reduce toil

- **Trigger phrases**: "Reduce toil", "I need to reduce toil", "Help me reduce toil"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Reduce toil
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Manage incident

- **Trigger phrases**: "Manage incident", "I need to manage incident", "Help me manage incident"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage incident
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

# ⌚ Wearable Technology Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Wearable Technology Operations domain.

### Intent 1: Manage wearable fleet

- **Trigger phrases**: "Manage wearable fleet", "I need to manage wearable fleet", "Help me manage wearable fleet"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage wearable fleet
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Process health data

- **Trigger phrases**: "Process health data", "I need to process health data", "Help me process health data"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Process health data
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Push firmware update

- **Trigger phrases**: "Push firmware update", "I need to push firmware update", "Help me push firmware update"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Push firmware update
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Check privacy compliance

- **Trigger phrases**: "Check privacy compliance", "I need to check privacy compliance", "Help me check privacy compliance"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check privacy compliance
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Analyse health metrics

- **Trigger phrases**: "Analyse health metrics", "I need to analyse health metrics", "Help me analyse health metrics"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Analyse health metrics
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Set health alert

- **Trigger phrases**: "Set health alert", "I need to set health alert", "Help me set health alert"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Set health alert
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

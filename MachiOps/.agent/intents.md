# ⚙️ Machinery Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Machinery Operations domain.

### Intent 1: Monitor machine health

- **Trigger phrases**: "Monitor machine health", "I need to monitor machine health", "Help me monitor machine health"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Monitor machine health
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Predict failure

- **Trigger phrases**: "Predict failure", "I need to predict failure", "Help me predict failure"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Predict failure
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Manage equipment lifecycle

- **Trigger phrases**: "Manage equipment lifecycle", "I need to manage equipment lifecycle", "Help me manage equipment lifecycle"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage equipment lifecycle
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Analyse vibration

- **Trigger phrases**: "Analyse vibration", "I need to analyse vibration", "Help me analyse vibration"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Analyse vibration
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Integrate SCADA

- **Trigger phrases**: "Integrate SCADA", "I need to integrate scada", "Help me integrate scada"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Integrate SCADA
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Calculate OEE

- **Trigger phrases**: "Calculate OEE", "I need to calculate oee", "Help me calculate oee"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Calculate OEE
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

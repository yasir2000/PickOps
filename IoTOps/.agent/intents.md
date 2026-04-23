# 📡 IoT Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the IoT Operations domain.

### Intent 1: Manage device fleet

- **Trigger phrases**: "Manage device fleet", "I need to manage device fleet", "Help me manage device fleet"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage device fleet
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Push firmware update

- **Trigger phrases**: "Push firmware update", "I need to push firmware update", "Help me push firmware update"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Push firmware update
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Ingest telemetry

- **Trigger phrases**: "Ingest telemetry", "I need to ingest telemetry", "Help me ingest telemetry"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Ingest telemetry
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Deploy edge workload

- **Trigger phrases**: "Deploy edge workload", "I need to deploy edge workload", "Help me deploy edge workload"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Deploy edge workload
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Secure device

- **Trigger phrases**: "Secure device", "I need to secure device", "Help me secure device"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Secure device
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Create digital twin

- **Trigger phrases**: "Create digital twin", "I need to create digital twin", "Help me create digital twin"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Create digital twin
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

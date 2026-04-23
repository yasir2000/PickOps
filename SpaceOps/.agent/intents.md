# 🚀 Space Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Space Operations domain.

### Intent 1: Process telemetry

- **Trigger phrases**: "Process telemetry", "I need to process telemetry", "Help me process telemetry"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Process telemetry
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Manage satellite

- **Trigger phrases**: "Manage satellite", "I need to manage satellite", "Help me manage satellite"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage satellite
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Operate ground station

- **Trigger phrases**: "Operate ground station", "I need to operate ground station", "Help me operate ground station"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Operate ground station
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Plan mission

- **Trigger phrases**: "Plan mission", "I need to plan mission", "Help me plan mission"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Plan mission
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Calculate maneuver

- **Trigger phrases**: "Calculate maneuver", "I need to calculate maneuver", "Help me calculate maneuver"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Calculate maneuver
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Monitor space weather

- **Trigger phrases**: "Monitor space weather", "I need to monitor space weather", "Help me monitor space weather"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Monitor space weather
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

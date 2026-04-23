# 🔬 Microservices Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Microservices Operations domain.

### Intent 1: Set up service mesh

- **Trigger phrases**: "Set up service mesh", "I need to set up service mesh", "Help me set up service mesh"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Set up service mesh
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Trace request flow

- **Trigger phrases**: "Trace request flow", "I need to trace request flow", "Help me trace request flow"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Trace request flow
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Run chaos experiment

- **Trigger phrases**: "Run chaos experiment", "I need to run chaos experiment", "Help me run chaos experiment"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Run chaos experiment
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Configure API gateway

- **Trigger phrases**: "Configure API gateway", "I need to configure api gateway", "Help me configure api gateway"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Configure API gateway
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Manage service discovery

- **Trigger phrases**: "Manage service discovery", "I need to manage service discovery", "Help me manage service discovery"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage service discovery
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Set circuit breaker

- **Trigger phrases**: "Set circuit breaker", "I need to set circuit breaker", "Help me set circuit breaker"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Set circuit breaker
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

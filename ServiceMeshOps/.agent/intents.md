# 🕸️ Service Mesh Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Service Mesh Operations domain.

### Intent 1: Configure traffic routing

- **Trigger phrases**: "Configure traffic routing", "I need to configure traffic routing", "Help me configure traffic routing"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Configure traffic routing
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Enforce mTLS

- **Trigger phrases**: "Enforce mTLS", "I need to enforce mtls", "Help me enforce mtls"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Enforce mTLS
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Observe service traffic

- **Trigger phrases**: "Observe service traffic", "I need to observe service traffic", "Help me observe service traffic"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Observe service traffic
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Enforce policy

- **Trigger phrases**: "Enforce policy", "I need to enforce policy", "Help me enforce policy"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Enforce policy
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Set up canary route

- **Trigger phrases**: "Set up canary route", "I need to set up canary route", "Help me set up canary route"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Set up canary route
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Manage multi-cluster mesh

- **Trigger phrases**: "Manage multi-cluster mesh", "I need to manage multi-cluster mesh", "Help me manage multi-cluster mesh"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage multi-cluster mesh
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

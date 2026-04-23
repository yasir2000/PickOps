# 🔀 Git Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Git Operations domain.

### Intent 1: Sync cluster with Git

- **Trigger phrases**: "Sync cluster with Git", "I need to sync cluster with git", "Help me sync cluster with git"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Sync cluster with Git
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Detect config drift

- **Trigger phrases**: "Detect config drift", "I need to detect config drift", "Help me detect config drift"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Detect config drift
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Reconcile state

- **Trigger phrases**: "Reconcile state", "I need to reconcile state", "Help me reconcile state"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Reconcile state
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Manage secrets

- **Trigger phrases**: "Manage secrets", "I need to manage secrets", "Help me manage secrets"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage secrets
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Manage multi-cluster

- **Trigger phrases**: "Manage multi-cluster", "I need to manage multi-cluster", "Help me manage multi-cluster"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage multi-cluster
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Enforce PR workflow

- **Trigger phrases**: "Enforce PR workflow", "I need to enforce pr workflow", "Help me enforce pr workflow"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Enforce PR workflow
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

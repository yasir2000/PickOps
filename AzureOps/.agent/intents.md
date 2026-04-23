# 🔷 Azure Cloud Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Azure Cloud Operations domain.

### Intent 1: Deploy Azure resource

- **Trigger phrases**: "Deploy Azure resource", "I need to deploy azure resource", "Help me deploy azure resource"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Deploy Azure resource
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Enforce governance policy

- **Trigger phrases**: "Enforce governance policy", "I need to enforce governance policy", "Help me enforce governance policy"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Enforce governance policy
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Check budget status

- **Trigger phrases**: "Check budget status", "I need to check budget status", "Help me check budget status"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check budget status
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Manage AD group

- **Trigger phrases**: "Manage AD group", "I need to manage ad group", "Help me manage ad group"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage AD group
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Scale AKS cluster

- **Trigger phrases**: "Scale AKS cluster", "I need to scale aks cluster", "Help me scale aks cluster"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Scale AKS cluster
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Audit Azure environment

- **Trigger phrases**: "Audit Azure environment", "I need to audit azure environment", "Help me audit azure environment"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Audit Azure environment
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

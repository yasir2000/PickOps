# 🌐 National Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the National Operations domain.

### Intent 1: Manage digital identity

- **Trigger phrases**: "Manage digital identity", "I need to manage digital identity", "Help me manage digital identity"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage digital identity
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Share data across ministries

- **Trigger phrases**: "Share data across ministries", "I need to share data across ministries", "Help me share data across ministries"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Share data across ministries
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Operate data platform

- **Trigger phrases**: "Operate data platform", "I need to operate data platform", "Help me operate data platform"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Operate data platform
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Govern cybersecurity

- **Trigger phrases**: "Govern cybersecurity", "I need to govern cybersecurity", "Help me govern cybersecurity"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Govern cybersecurity
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Implement policy

- **Trigger phrases**: "Implement policy", "I need to implement policy", "Help me implement policy"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Implement policy
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Publish open data

- **Trigger phrases**: "Publish open data", "I need to publish open data", "Help me publish open data"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Publish open data
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

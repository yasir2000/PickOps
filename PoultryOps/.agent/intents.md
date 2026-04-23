# 🐔 Poultry Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Poultry Operations domain.

### Intent 1: Monitor flock health

- **Trigger phrases**: "Monitor flock health", "I need to monitor flock health", "Help me monitor flock health"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Monitor flock health
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Manage feed

- **Trigger phrases**: "Manage feed", "I need to manage feed", "Help me manage feed"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage feed
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Enforce biosecurity

- **Trigger phrases**: "Enforce biosecurity", "I need to enforce biosecurity", "Help me enforce biosecurity"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Enforce biosecurity
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Track egg production

- **Trigger phrases**: "Track egg production", "I need to track egg production", "Help me track egg production"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track egg production
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Control environment

- **Trigger phrases**: "Control environment", "I need to control environment", "Help me control environment"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Control environment
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Schedule slaughter

- **Trigger phrases**: "Schedule slaughter", "I need to schedule slaughter", "Help me schedule slaughter"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Schedule slaughter
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

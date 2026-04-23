# 🚆 Transportation Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Transportation Operations domain.

### Intent 1: Manage transport network

- **Trigger phrases**: "Manage transport network", "I need to manage transport network", "Help me manage transport network"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage transport network
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Optimize schedule

- **Trigger phrases**: "Optimize schedule", "I need to optimize schedule", "Help me optimize schedule"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Optimize schedule
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Track vehicle

- **Trigger phrases**: "Track vehicle", "I need to track vehicle", "Help me track vehicle"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track vehicle
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Enhance passenger experience

- **Trigger phrases**: "Enhance passenger experience", "I need to enhance passenger experience", "Help me enhance passenger experience"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Enhance passenger experience
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Schedule maintenance

- **Trigger phrases**: "Schedule maintenance", "I need to schedule maintenance", "Help me schedule maintenance"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Schedule maintenance
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Optimize revenue

- **Trigger phrases**: "Optimize revenue", "I need to optimize revenue", "Help me optimize revenue"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Optimize revenue
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

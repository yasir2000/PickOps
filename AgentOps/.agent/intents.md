# 🤖 AI Agent Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the AI Agent Operations domain.

### Intent 1: Deploy a new agent

- **Trigger phrases**: "Deploy a new agent", "I need to deploy a new agent", "Help me deploy a new agent"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Deploy a new agent
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Monitor agent performance

- **Trigger phrases**: "Monitor agent performance", "I need to monitor agent performance", "Help me monitor agent performance"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Monitor agent performance
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Debug a failing agent

- **Trigger phrases**: "Debug a failing agent", "I need to debug a failing agent", "Help me debug a failing agent"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Debug a failing agent
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Chain agents together

- **Trigger phrases**: "Chain agents together", "I need to chain agents together", "Help me chain agents together"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Chain agents together
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Evaluate agent output quality

- **Trigger phrases**: "Evaluate agent output quality", "I need to evaluate agent output quality", "Help me evaluate agent output quality"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Evaluate agent output quality
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Add a new tool to an agent

- **Trigger phrases**: "Add a new tool to an agent", "I need to add a new tool to an agent", "Help me add a new tool to an agent"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Add a new tool to an agent
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

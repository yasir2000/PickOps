# 🤖 Machine Learning Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Machine Learning Operations domain.

### Intent 1: Train ML model

- **Trigger phrases**: "Train ML model", "I need to train ml model", "Help me train ml model"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Train ML model
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Register model version

- **Trigger phrases**: "Register model version", "I need to register model version", "Help me register model version"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Register model version
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Deploy model endpoint

- **Trigger phrases**: "Deploy model endpoint", "I need to deploy model endpoint", "Help me deploy model endpoint"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Deploy model endpoint
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Detect model drift

- **Trigger phrases**: "Detect model drift", "I need to detect model drift", "Help me detect model drift"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Detect model drift
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Manage features

- **Trigger phrases**: "Manage features", "I need to manage features", "Help me manage features"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage features
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Track experiment

- **Trigger phrases**: "Track experiment", "I need to track experiment", "Help me track experiment"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track experiment
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

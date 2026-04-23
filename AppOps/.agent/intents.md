# 📱 Application Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Application Operations domain.

### Intent 1: Deploy new version

- **Trigger phrases**: "Deploy new version", "I need to deploy new version", "Help me deploy new version"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Deploy new version
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Toggle feature flag

- **Trigger phrases**: "Toggle feature flag", "I need to toggle feature flag", "Help me toggle feature flag"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Toggle feature flag
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Investigate error spike

- **Trigger phrases**: "Investigate error spike", "I need to investigate error spike", "Help me investigate error spike"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Investigate error spike
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Check app performance

- **Trigger phrases**: "Check app performance", "I need to check app performance", "Help me check app performance"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check app performance
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Set up A/B test

- **Trigger phrases**: "Set up A/B test", "I need to set up a/b test", "Help me set up a/b test"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Set up A/B test
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Roll back last deployment

- **Trigger phrases**: "Roll back last deployment", "I need to roll back last deployment", "Help me roll back last deployment"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Roll back last deployment
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

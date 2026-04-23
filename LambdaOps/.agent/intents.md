# λ Serverless Lambda Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Serverless Lambda Operations domain.

### Intent 1: Deploy serverless function

- **Trigger phrases**: "Deploy serverless function", "I need to deploy serverless function", "Help me deploy serverless function"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Deploy serverless function
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Reduce cold starts

- **Trigger phrases**: "Reduce cold starts", "I need to reduce cold starts", "Help me reduce cold starts"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Reduce cold starts
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Monitor function metrics

- **Trigger phrases**: "Monitor function metrics", "I need to monitor function metrics", "Help me monitor function metrics"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Monitor function metrics
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Optimize costs

- **Trigger phrases**: "Optimize costs", "I need to optimize costs", "Help me optimize costs"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Optimize costs
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Manage event source

- **Trigger phrases**: "Manage event source", "I need to manage event source", "Help me manage event source"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage event source
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Secure function

- **Trigger phrases**: "Secure function", "I need to secure function", "Help me secure function"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Secure function
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

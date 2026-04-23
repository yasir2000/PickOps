# 🔧 Development Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Development Operations domain.

### Intent 1: Set up CI/CD pipeline

- **Trigger phrases**: "Set up CI/CD pipeline", "I need to set up ci/cd pipeline", "Help me set up ci/cd pipeline"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Set up CI/CD pipeline
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Provision infrastructure

- **Trigger phrases**: "Provision infrastructure", "I need to provision infrastructure", "Help me provision infrastructure"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Provision infrastructure
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Create release gate

- **Trigger phrases**: "Create release gate", "I need to create release gate", "Help me create release gate"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Create release gate
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Deploy to Kubernetes

- **Trigger phrases**: "Deploy to Kubernetes", "I need to deploy to kubernetes", "Help me deploy to kubernetes"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Deploy to Kubernetes
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Set up monitoring

- **Trigger phrases**: "Set up monitoring", "I need to set up monitoring", "Help me set up monitoring"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Set up monitoring
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Improve build times

- **Trigger phrases**: "Improve build times", "I need to improve build times", "Help me improve build times"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Improve build times
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

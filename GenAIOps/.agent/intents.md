# ✨ Generative AI Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Generative AI Operations domain.

### Intent 1: Deploy LLM

- **Trigger phrases**: "Deploy LLM", "I need to deploy llm", "Help me deploy llm"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Deploy LLM
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Manage prompt versions

- **Trigger phrases**: "Manage prompt versions", "I need to manage prompt versions", "Help me manage prompt versions"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage prompt versions
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Evaluate model quality

- **Trigger phrases**: "Evaluate model quality", "I need to evaluate model quality", "Help me evaluate model quality"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Evaluate model quality
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Apply safety guardrails

- **Trigger phrases**: "Apply safety guardrails", "I need to apply safety guardrails", "Help me apply safety guardrails"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Apply safety guardrails
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Fine-tune model

- **Trigger phrases**: "Fine-tune model", "I need to fine-tune model", "Help me fine-tune model"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Fine-tune model
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Optimize LLM costs

- **Trigger phrases**: "Optimize LLM costs", "I need to optimize llm costs", "Help me optimize llm costs"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Optimize LLM costs
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

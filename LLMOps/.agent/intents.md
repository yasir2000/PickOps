# 🧬 Large Language Model Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Large Language Model Operations domain.

### Intent 1: Deploy LLM endpoint

- **Trigger phrases**: "Deploy LLM endpoint", "I need to deploy llm endpoint", "Help me deploy llm endpoint"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Deploy LLM endpoint
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Run fine-tuning job

- **Trigger phrases**: "Run fine-tuning job", "I need to run fine-tuning job", "Help me run fine-tuning job"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Run fine-tuning job
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Evaluate model

- **Trigger phrases**: "Evaluate model", "I need to evaluate model", "Help me evaluate model"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Evaluate model
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Optimize prompt

- **Trigger phrases**: "Optimize prompt", "I need to optimize prompt", "Help me optimize prompt"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Optimize prompt
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Monitor LLM costs

- **Trigger phrases**: "Monitor LLM costs", "I need to monitor llm costs", "Help me monitor llm costs"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Monitor LLM costs
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Apply safety filter

- **Trigger phrases**: "Apply safety filter", "I need to apply safety filter", "Help me apply safety filter"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Apply safety filter
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

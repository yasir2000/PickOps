# 🔭 Scientific Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Scientific Operations domain.

### Intent 1: Run scientific workflow

- **Trigger phrases**: "Run scientific workflow", "I need to run scientific workflow", "Help me run scientific workflow"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Run scientific workflow
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Submit HPC job

- **Trigger phrases**: "Submit HPC job", "I need to submit hpc job", "Help me submit hpc job"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Submit HPC job
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Track experiment

- **Trigger phrases**: "Track experiment", "I need to track experiment", "Help me track experiment"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track experiment
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Store scientific data

- **Trigger phrases**: "Store scientific data", "I need to store scientific data", "Help me store scientific data"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Store scientific data
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Run simulation

- **Trigger phrases**: "Run simulation", "I need to run simulation", "Help me run simulation"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Run simulation
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Submit publication

- **Trigger phrases**: "Submit publication", "I need to submit publication", "Help me submit publication"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Submit publication
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

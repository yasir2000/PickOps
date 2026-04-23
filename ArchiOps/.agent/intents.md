# 🏛️ Architecture & Design Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Architecture & Design Operations domain.

### Intent 1: Upload new BIM model

- **Trigger phrases**: "Upload new BIM model", "I need to upload new bim model", "Help me upload new bim model"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Upload new BIM model
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Check planning compliance

- **Trigger phrases**: "Check planning compliance", "I need to check planning compliance", "Help me check planning compliance"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check planning compliance
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Coordinate with structural team

- **Trigger phrases**: "Coordinate with structural team", "I need to coordinate with structural team", "Help me coordinate with structural team"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Coordinate with structural team
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Estimate project cost

- **Trigger phrases**: "Estimate project cost", "I need to estimate project cost", "Help me estimate project cost"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Estimate project cost
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Review energy performance

- **Trigger phrases**: "Review energy performance", "I need to review energy performance", "Help me review energy performance"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Review energy performance
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Produce drawing set

- **Trigger phrases**: "Produce drawing set", "I need to produce drawing set", "Help me produce drawing set"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Produce drawing set
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

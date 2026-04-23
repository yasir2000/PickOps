# 💊 Pharmaceutical Drug Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Pharmaceutical Drug Operations domain.

### Intent 1: Check GMP compliance

- **Trigger phrases**: "Check GMP compliance", "I need to check gmp compliance", "Help me check gmp compliance"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check GMP compliance
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Manage clinical data

- **Trigger phrases**: "Manage clinical data", "I need to manage clinical data", "Help me manage clinical data"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage clinical data
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Prepare FDA submission

- **Trigger phrases**: "Prepare FDA submission", "I need to prepare fda submission", "Help me prepare fda submission"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Prepare FDA submission
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Monitor adverse events

- **Trigger phrases**: "Monitor adverse events", "I need to monitor adverse events", "Help me monitor adverse events"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Monitor adverse events
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Track cold chain

- **Trigger phrases**: "Track cold chain", "I need to track cold chain", "Help me track cold chain"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track cold chain
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Generate batch record

- **Trigger phrases**: "Generate batch record", "I need to generate batch record", "Help me generate batch record"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Generate batch record
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

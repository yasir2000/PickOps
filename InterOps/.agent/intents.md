# 🔗 Interoperability Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Interoperability Operations domain.

### Intent 1: Integrate two systems

- **Trigger phrases**: "Integrate two systems", "I need to integrate two systems", "Help me integrate two systems"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Integrate two systems
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Translate data format

- **Trigger phrases**: "Translate data format", "I need to translate data format", "Help me translate data format"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Translate data format
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Bridge protocols

- **Trigger phrases**: "Bridge protocols", "I need to bridge protocols", "Help me bridge protocols"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Bridge protocols
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Test integration

- **Trigger phrases**: "Test integration", "I need to test integration", "Help me test integration"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Test integration
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Set up event flow

- **Trigger phrases**: "Set up event flow", "I need to set up event flow", "Help me set up event flow"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Set up event flow
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Govern API

- **Trigger phrases**: "Govern API", "I need to govern api", "Help me govern api"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Govern API
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

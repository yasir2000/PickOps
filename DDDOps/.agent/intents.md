# 🗺️ Domain-Driven Design Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Domain-Driven Design Operations domain.

### Intent 1: Map bounded context

- **Trigger phrases**: "Map bounded context", "I need to map bounded context", "Help me map bounded context"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Map bounded context
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Run event storming

- **Trigger phrases**: "Run event storming", "I need to run event storming", "Help me run event storming"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Run event storming
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Version domain model

- **Trigger phrases**: "Version domain model", "I need to version domain model", "Help me version domain model"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Version domain model
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Visualize context map

- **Trigger phrases**: "Visualize context map", "I need to visualize context map", "Help me visualize context map"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Visualize context map
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Enforce language consistency

- **Trigger phrases**: "Enforce language consistency", "I need to enforce language consistency", "Help me enforce language consistency"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Enforce language consistency
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Detect boundary violation

- **Trigger phrases**: "Detect boundary violation", "I need to detect boundary violation", "Help me detect boundary violation"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Detect boundary violation
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

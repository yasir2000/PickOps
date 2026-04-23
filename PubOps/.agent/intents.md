# 📚 Publishing Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Publishing Operations domain.

### Intent 1: Submit manuscript

- **Trigger phrases**: "Submit manuscript", "I need to submit manuscript", "Help me submit manuscript"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Submit manuscript
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Run editorial review

- **Trigger phrases**: "Run editorial review", "I need to run editorial review", "Help me run editorial review"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Run editorial review
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Manage production

- **Trigger phrases**: "Manage production", "I need to manage production", "Help me manage production"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage production
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Distribute publication

- **Trigger phrases**: "Distribute publication", "I need to distribute publication", "Help me distribute publication"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Distribute publication
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Track rights

- **Trigger phrases**: "Track rights", "I need to track rights", "Help me track rights"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track rights
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Manage metadata

- **Trigger phrases**: "Manage metadata", "I need to manage metadata", "Help me manage metadata"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage metadata
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

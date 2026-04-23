# 🔬 Research Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Research Operations domain.

### Intent 1: Manage research data

- **Trigger phrases**: "Manage research data", "I need to manage research data", "Help me manage research data"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage research data
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Build analysis pipeline

- **Trigger phrases**: "Build analysis pipeline", "I need to build analysis pipeline", "Help me build analysis pipeline"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Build analysis pipeline
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Review literature

- **Trigger phrases**: "Review literature", "I need to review literature", "Help me review literature"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Review literature
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Submit publication

- **Trigger phrases**: "Submit publication", "I need to submit publication", "Help me submit publication"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Submit publication
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Coordinate team

- **Trigger phrases**: "Coordinate team", "I need to coordinate team", "Help me coordinate team"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Coordinate team
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Track grant

- **Trigger phrases**: "Track grant", "I need to track grant", "Help me track grant"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track grant
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

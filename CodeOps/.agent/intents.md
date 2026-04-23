# 💻 Code Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Code Operations domain.

### Intent 1: Analyse code quality

- **Trigger phrases**: "Analyse code quality", "I need to analyse code quality", "Help me analyse code quality"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Analyse code quality
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Scan for vulnerable dependencies

- **Trigger phrases**: "Scan for vulnerable dependencies", "I need to scan for vulnerable dependencies", "Help me scan for vulnerable dependencies"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Scan for vulnerable dependencies
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Review PR automatically

- **Trigger phrases**: "Review PR automatically", "I need to review pr automatically", "Help me review pr automatically"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Review PR automatically
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Check test coverage

- **Trigger phrases**: "Check test coverage", "I need to check test coverage", "Help me check test coverage"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check test coverage
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Measure tech debt

- **Trigger phrases**: "Measure tech debt", "I need to measure tech debt", "Help me measure tech debt"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Measure tech debt
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Track deployment frequency

- **Trigger phrases**: "Track deployment frequency", "I need to track deployment frequency", "Help me track deployment frequency"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track deployment frequency
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

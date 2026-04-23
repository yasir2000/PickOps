# 🎬 Animation & Media Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Animation & Media Operations domain.

### Intent 1: Submit render job

- **Trigger phrases**: "Submit render job", "I need to submit render job", "Help me submit render job"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Submit render job
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Check render status

- **Trigger phrases**: "Check render status", "I need to check render status", "Help me check render status"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check render status
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Find latest version of asset

- **Trigger phrases**: "Find latest version of asset", "I need to find latest version of asset", "Help me find latest version of asset"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Find latest version of asset
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Schedule artist tasks

- **Trigger phrases**: "Schedule artist tasks", "I need to schedule artist tasks", "Help me schedule artist tasks"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Schedule artist tasks
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Flag frame quality issues

- **Trigger phrases**: "Flag frame quality issues", "I need to flag frame quality issues", "Help me flag frame quality issues"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Flag frame quality issues
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Generate production report

- **Trigger phrases**: "Generate production report", "I need to generate production report", "Help me generate production report"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Generate production report
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

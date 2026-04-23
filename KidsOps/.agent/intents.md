# 🧒 Kids & Family Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Kids & Family Operations domain.

### Intent 1: Filter unsafe content

- **Trigger phrases**: "Filter unsafe content", "I need to filter unsafe content", "Help me filter unsafe content"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Filter unsafe content
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Set parental control

- **Trigger phrases**: "Set parental control", "I need to set parental control", "Help me set parental control"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Set parental control
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Schedule activity

- **Trigger phrases**: "Schedule activity", "I need to schedule activity", "Help me schedule activity"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Schedule activity
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Curate educational content

- **Trigger phrases**: "Curate educational content", "I need to curate educational content", "Help me curate educational content"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Curate educational content
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Track progress

- **Trigger phrases**: "Track progress", "I need to track progress", "Help me track progress"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track progress
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Set screen time limit

- **Trigger phrases**: "Set screen time limit", "I need to set screen time limit", "Help me set screen time limit"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Set screen time limit
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

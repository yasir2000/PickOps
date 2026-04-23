# 🎭 Entertainment Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Entertainment Operations domain.

### Intent 1: Track content production

- **Trigger phrases**: "Track content production", "I need to track content production", "Help me track content production"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track content production
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Check rights status

- **Trigger phrases**: "Check rights status", "I need to check rights status", "Help me check rights status"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check rights status
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Analyse audience data

- **Trigger phrases**: "Analyse audience data", "I need to analyse audience data", "Help me analyse audience data"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Analyse audience data
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Distribute to streaming platform

- **Trigger phrases**: "Distribute to streaming platform", "I need to distribute to streaming platform", "Help me distribute to streaming platform"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Distribute to streaming platform
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Operate live event

- **Trigger phrases**: "Operate live event", "I need to operate live event", "Help me operate live event"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Operate live event
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Moderate content

- **Trigger phrases**: "Moderate content", "I need to moderate content", "Help me moderate content"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Moderate content
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

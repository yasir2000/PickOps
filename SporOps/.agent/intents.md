# ⚽ Sports Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Sports Operations domain.

### Intent 1: Analyse athlete performance

- **Trigger phrases**: "Analyse athlete performance", "I need to analyse athlete performance", "Help me analyse athlete performance"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Analyse athlete performance
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Manage team schedule

- **Trigger phrases**: "Manage team schedule", "I need to manage team schedule", "Help me manage team schedule"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage team schedule
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Engage fans

- **Trigger phrases**: "Engage fans", "I need to engage fans", "Help me engage fans"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Engage fans
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Operate venue

- **Trigger phrases**: "Operate venue", "I need to operate venue", "Help me operate venue"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Operate venue
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Coordinate broadcast

- **Trigger phrases**: "Coordinate broadcast", "I need to coordinate broadcast", "Help me coordinate broadcast"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Coordinate broadcast
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Check betting compliance

- **Trigger phrases**: "Check betting compliance", "I need to check betting compliance", "Help me check betting compliance"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check betting compliance
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

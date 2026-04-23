# ✈️ Aviation Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Aviation Operations domain.

### Intent 1: Schedule crew for next week

- **Trigger phrases**: "Schedule crew for next week", "I need to schedule crew for next week", "Help me schedule crew for next week"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Schedule crew for next week
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Check aircraft maintenance status

- **Trigger phrases**: "Check aircraft maintenance status", "I need to check aircraft maintenance status", "Help me check aircraft maintenance status"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check aircraft maintenance status
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Parse incoming NOTAM

- **Trigger phrases**: "Parse incoming NOTAM", "I need to parse incoming notam", "Help me parse incoming notam"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Parse incoming NOTAM
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Calculate optimal fuel load

- **Trigger phrases**: "Calculate optimal fuel load", "I need to calculate optimal fuel load", "Help me calculate optimal fuel load"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Calculate optimal fuel load
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Generate pre-flight safety checklist

- **Trigger phrases**: "Generate pre-flight safety checklist", "I need to generate pre-flight safety checklist", "Help me generate pre-flight safety checklist"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Generate pre-flight safety checklist
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Report a safety incident

- **Trigger phrases**: "Report a safety incident", "I need to report a safety incident", "Help me report a safety incident"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Report a safety incident
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

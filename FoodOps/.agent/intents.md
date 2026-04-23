# 🍽️ Food Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Food Operations domain.

### Intent 1: Check HACCP status

- **Trigger phrases**: "Check HACCP status", "I need to check haccp status", "Help me check haccp status"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check HACCP status
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Schedule production

- **Trigger phrases**: "Schedule production", "I need to schedule production", "Help me schedule production"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Schedule production
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Run QC check

- **Trigger phrases**: "Run QC check", "I need to run qc check", "Help me run qc check"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Run QC check
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Track product origin

- **Trigger phrases**: "Track product origin", "I need to track product origin", "Help me track product origin"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track product origin
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Check allergen info

- **Trigger phrases**: "Check allergen info", "I need to check allergen info", "Help me check allergen info"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check allergen info
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Generate compliance report

- **Trigger phrases**: "Generate compliance report", "I need to generate compliance report", "Help me generate compliance report"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Generate compliance report
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

# 🏥 Healthcare Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Healthcare Operations domain.

### Intent 1: Access patient record

- **Trigger phrases**: "Access patient record", "I need to access patient record", "Help me access patient record"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Access patient record
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Document clinical note

- **Trigger phrases**: "Document clinical note", "I need to document clinical note", "Help me document clinical note"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Document clinical note
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Check HIPAA compliance

- **Trigger phrases**: "Check HIPAA compliance", "I need to check hipaa compliance", "Help me check hipaa compliance"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check HIPAA compliance
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Monitor device

- **Trigger phrases**: "Monitor device", "I need to monitor device", "Help me monitor device"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Monitor device
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Analyse patient outcomes

- **Trigger phrases**: "Analyse patient outcomes", "I need to analyse patient outcomes", "Help me analyse patient outcomes"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Analyse patient outcomes
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Coordinate care team

- **Trigger phrases**: "Coordinate care team", "I need to coordinate care team", "Help me coordinate care team"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Coordinate care team
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

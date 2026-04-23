# ⚖️ Legal Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Legal Operations domain.

### Intent 1: Draft contract

- **Trigger phrases**: "Draft contract", "I need to draft contract", "Help me draft contract"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Draft contract
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Track legal matter

- **Trigger phrases**: "Track legal matter", "I need to track legal matter", "Help me track legal matter"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track legal matter
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Process invoice

- **Trigger phrases**: "Process invoice", "I need to process invoice", "Help me process invoice"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Process invoice
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Check compliance

- **Trigger phrases**: "Check compliance", "I need to check compliance", "Help me check compliance"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check compliance
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Research legal topic

- **Trigger phrases**: "Research legal topic", "I need to research legal topic", "Help me research legal topic"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Research legal topic
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Review document

- **Trigger phrases**: "Review document", "I need to review document", "Help me review document"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Review document
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

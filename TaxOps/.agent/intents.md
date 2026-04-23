# 🧾 Tax Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Tax Operations domain.

### Intent 1: Check tax compliance

- **Trigger phrases**: "Check tax compliance", "I need to check tax compliance", "Help me check tax compliance"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check tax compliance
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: File tax return

- **Trigger phrases**: "File tax return", "I need to file tax return", "Help me file tax return"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: File tax return
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Manage international tax

- **Trigger phrases**: "Manage international tax", "I need to manage international tax", "Help me manage international tax"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage international tax
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Document transfer pricing

- **Trigger phrases**: "Document transfer pricing", "I need to document transfer pricing", "Help me document transfer pricing"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Document transfer pricing
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Prepare audit trail

- **Trigger phrases**: "Prepare audit trail", "I need to prepare audit trail", "Help me prepare audit trail"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Prepare audit trail
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Calculate VAT/GST

- **Trigger phrases**: "Calculate VAT/GST", "I need to calculate vat/gst", "Help me calculate vat/gst"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Calculate VAT/GST
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

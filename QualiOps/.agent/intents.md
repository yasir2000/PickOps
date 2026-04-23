# ✅ Quality Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Quality Operations domain.

### Intent 1: Run quality inspection

- **Trigger phrases**: "Run quality inspection", "I need to run quality inspection", "Help me run quality inspection"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Run quality inspection
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Log non-conformance

- **Trigger phrases**: "Log non-conformance", "I need to log non-conformance", "Help me log non-conformance"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Log non-conformance
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Initiate corrective action

- **Trigger phrases**: "Initiate corrective action", "I need to initiate corrective action", "Help me initiate corrective action"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Initiate corrective action
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Apply SPC analysis

- **Trigger phrases**: "Apply SPC analysis", "I need to apply spc analysis", "Help me apply spc analysis"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Apply SPC analysis
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Manage supplier quality

- **Trigger phrases**: "Manage supplier quality", "I need to manage supplier quality", "Help me manage supplier quality"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage supplier quality
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Conduct audit

- **Trigger phrases**: "Conduct audit", "I need to conduct audit", "Help me conduct audit"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Conduct audit
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

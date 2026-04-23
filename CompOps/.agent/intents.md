# ⚖️ Compliance Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Compliance Operations domain.

### Intent 1: Check compliance posture

- **Trigger phrases**: "Check compliance posture", "I need to check compliance posture", "Help me check compliance posture"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check compliance posture
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Collect audit evidence

- **Trigger phrases**: "Collect audit evidence", "I need to collect audit evidence", "Help me collect audit evidence"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Collect audit evidence
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Map control to regulation

- **Trigger phrases**: "Map control to regulation", "I need to map control to regulation", "Help me map control to regulation"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Map control to regulation
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Assess risk

- **Trigger phrases**: "Assess risk", "I need to assess risk", "Help me assess risk"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Assess risk
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Generate audit report

- **Trigger phrases**: "Generate audit report", "I need to generate audit report", "Help me generate audit report"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Generate audit report
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Alert on policy violation

- **Trigger phrases**: "Alert on policy violation", "I need to alert on policy violation", "Help me alert on policy violation"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Alert on policy violation
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

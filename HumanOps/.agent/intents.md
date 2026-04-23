# 👥 Human Resources Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Human Resources Operations domain.

### Intent 1: Post job and screen candidates

- **Trigger phrases**: "Post job and screen candidates", "I need to post job and screen candidates", "Help me post job and screen candidates"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Post job and screen candidates
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Onboard new employee

- **Trigger phrases**: "Onboard new employee", "I need to onboard new employee", "Help me onboard new employee"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Onboard new employee
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Run performance review

- **Trigger phrases**: "Run performance review", "I need to run performance review", "Help me run performance review"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Run performance review
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Process payroll

- **Trigger phrases**: "Process payroll", "I need to process payroll", "Help me process payroll"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Process payroll
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Check HR compliance

- **Trigger phrases**: "Check HR compliance", "I need to check hr compliance", "Help me check hr compliance"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check HR compliance
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Analyse workforce metrics

- **Trigger phrases**: "Analyse workforce metrics", "I need to analyse workforce metrics", "Help me analyse workforce metrics"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Analyse workforce metrics
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

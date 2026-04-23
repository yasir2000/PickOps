# 🔄 Application Lifecycle Management Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Application Lifecycle Management Operations domain.

### Intent 1: Trace requirement to test

- **Trigger phrases**: "Trace requirement to test", "I need to trace requirement to test", "Help me trace requirement to test"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Trace requirement to test
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Approve a change request

- **Trigger phrases**: "Approve a change request", "I need to approve a change request", "Help me approve a change request"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Approve a change request
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Generate release notes

- **Trigger phrases**: "Generate release notes", "I need to generate release notes", "Help me generate release notes"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Generate release notes
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Measure technical debt

- **Trigger phrases**: "Measure technical debt", "I need to measure technical debt", "Help me measure technical debt"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Measure technical debt
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Plan next quarter roadmap

- **Trigger phrases**: "Plan next quarter roadmap", "I need to plan next quarter roadmap", "Help me plan next quarter roadmap"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Plan next quarter roadmap
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Audit compliance status

- **Trigger phrases**: "Audit compliance status", "I need to audit compliance status", "Help me audit compliance status"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Audit compliance status
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

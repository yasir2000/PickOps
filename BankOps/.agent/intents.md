# 🏦 Banking Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Banking Operations domain.

### Intent 1: Process payment

- **Trigger phrases**: "Process payment", "I need to process payment", "Help me process payment"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Process payment
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Flag suspicious transaction

- **Trigger phrases**: "Flag suspicious transaction", "I need to flag suspicious transaction", "Help me flag suspicious transaction"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Flag suspicious transaction
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Run KYC check

- **Trigger phrases**: "Run KYC check", "I need to run kyc check", "Help me run kyc check"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Run KYC check
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Reconcile accounts

- **Trigger phrases**: "Reconcile accounts", "I need to reconcile accounts", "Help me reconcile accounts"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Reconcile accounts
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Generate Basel report

- **Trigger phrases**: "Generate Basel report", "I need to generate basel report", "Help me generate basel report"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Generate Basel report
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Monitor credit exposure

- **Trigger phrases**: "Monitor credit exposure", "I need to monitor credit exposure", "Help me monitor credit exposure"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Monitor credit exposure
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

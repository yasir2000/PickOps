# ☁️ AWS Cloud Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the AWS Cloud Operations domain.

### Intent 1: Provision new environment

- **Trigger phrases**: "Provision new environment", "I need to provision new environment", "Help me provision new environment"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Provision new environment
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Find cost anomalies

- **Trigger phrases**: "Find cost anomalies", "I need to find cost anomalies", "Help me find cost anomalies"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Find cost anomalies
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Check security posture

- **Trigger phrases**: "Check security posture", "I need to check security posture", "Help me check security posture"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check security posture
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Manage AWS accounts

- **Trigger phrases**: "Manage AWS accounts", "I need to manage aws accounts", "Help me manage aws accounts"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage AWS accounts
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Run DR drill

- **Trigger phrases**: "Run DR drill", "I need to run dr drill", "Help me run dr drill"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Run DR drill
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Generate cost report

- **Trigger phrases**: "Generate cost report", "I need to generate cost report", "Help me generate cost report"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Generate cost report
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

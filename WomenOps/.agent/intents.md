# 👩‍💻 Women in Tech & DEI Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Women in Tech & DEI Operations domain.

### Intent 1: Analyse pay equity

- **Trigger phrases**: "Analyse pay equity", "I need to analyse pay equity", "Help me analyse pay equity"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Analyse pay equity
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Run inclusive hiring

- **Trigger phrases**: "Run inclusive hiring", "I need to run inclusive hiring", "Help me run inclusive hiring"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Run inclusive hiring
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Manage mentorship

- **Trigger phrases**: "Manage mentorship", "I need to manage mentorship", "Help me manage mentorship"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage mentorship
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Track DEI metrics

- **Trigger phrases**: "Track DEI metrics", "I need to track dei metrics", "Help me track dei metrics"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track DEI metrics
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Coordinate ERG

- **Trigger phrases**: "Coordinate ERG", "I need to coordinate erg", "Help me coordinate erg"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Coordinate ERG
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Detect bias

- **Trigger phrases**: "Detect bias", "I need to detect bias", "Help me detect bias"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Detect bias
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

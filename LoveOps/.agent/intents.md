# ❤️ Relationship & Wellbeing Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Relationship & Wellbeing Operations domain.

### Intent 1: Find compatible match

- **Trigger phrases**: "Find compatible match", "I need to find compatible match", "Help me find compatible match"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Find compatible match
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Get communication coaching

- **Trigger phrases**: "Get communication coaching", "I need to get communication coaching", "Help me get communication coaching"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Get communication coaching
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Access mental health resource

- **Trigger phrases**: "Access mental health resource", "I need to access mental health resource", "Help me access mental health resource"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Access mental health resource
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Report safety issue

- **Trigger phrases**: "Report safety issue", "I need to report safety issue", "Help me report safety issue"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Report safety issue
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Check privacy settings

- **Trigger phrases**: "Check privacy settings", "I need to check privacy settings", "Help me check privacy settings"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check privacy settings
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Analyse engagement

- **Trigger phrases**: "Analyse engagement", "I need to analyse engagement", "Help me analyse engagement"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Analyse engagement
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

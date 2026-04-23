# 🧠 Psychology & Mental Health Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Psychology & Mental Health Operations domain.

### Intent 1: Automate clinical workflow

- **Trigger phrases**: "Automate clinical workflow", "I need to automate clinical workflow", "Help me automate clinical workflow"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Automate clinical workflow
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Monitor patient progress

- **Trigger phrases**: "Monitor patient progress", "I need to monitor patient progress", "Help me monitor patient progress"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Monitor patient progress
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Start telehealth session

- **Trigger phrases**: "Start telehealth session", "I need to start telehealth session", "Help me start telehealth session"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Start telehealth session
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Route crisis call

- **Trigger phrases**: "Route crisis call", "I need to route crisis call", "Help me route crisis call"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Route crisis call
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Manage treatment plan

- **Trigger phrases**: "Manage treatment plan", "I need to manage treatment plan", "Help me manage treatment plan"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage treatment plan
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Check HIPAA compliance

- **Trigger phrases**: "Check HIPAA compliance", "I need to check hipaa compliance", "Help me check hipaa compliance"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check HIPAA compliance
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

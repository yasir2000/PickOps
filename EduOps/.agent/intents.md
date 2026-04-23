# 🎓 Education Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Education Operations domain.

### Intent 1: Update LMS course

- **Trigger phrases**: "Update LMS course", "I need to update lms course", "Help me update lms course"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Update LMS course
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Analyse student performance

- **Trigger phrases**: "Analyse student performance", "I need to analyse student performance", "Help me analyse student performance"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Analyse student performance
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Plan curriculum

- **Trigger phrases**: "Plan curriculum", "I need to plan curriculum", "Help me plan curriculum"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Plan curriculum
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Set up adaptive learning

- **Trigger phrases**: "Set up adaptive learning", "I need to set up adaptive learning", "Help me set up adaptive learning"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Set up adaptive learning
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Check accreditation status

- **Trigger phrases**: "Check accreditation status", "I need to check accreditation status", "Help me check accreditation status"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check accreditation status
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Generate institutional report

- **Trigger phrases**: "Generate institutional report", "I need to generate institutional report", "Help me generate institutional report"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Generate institutional report
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

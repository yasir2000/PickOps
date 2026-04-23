# 🛩️ Avionics Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Avionics Operations domain.

### Intent 1: Run avionics test suite

- **Trigger phrases**: "Run avionics test suite", "I need to run avionics test suite", "Help me run avionics test suite"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Run avionics test suite
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Check DO-178C compliance

- **Trigger phrases**: "Check DO-178C compliance", "I need to check do-178c compliance", "Help me check do-178c compliance"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check DO-178C compliance
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Push firmware update

- **Trigger phrases**: "Push firmware update", "I need to push firmware update", "Help me push firmware update"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Push firmware update
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Parse ARINC data stream

- **Trigger phrases**: "Parse ARINC data stream", "I need to parse arinc data stream", "Help me parse arinc data stream"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Parse ARINC data stream
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Isolate avionics fault

- **Trigger phrases**: "Isolate avionics fault", "I need to isolate avionics fault", "Help me isolate avionics fault"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Isolate avionics fault
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Generate certification report

- **Trigger phrases**: "Generate certification report", "I need to generate certification report", "Help me generate certification report"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Generate certification report
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

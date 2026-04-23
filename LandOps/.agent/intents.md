# 🗺️ Land Management Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Land Management Operations domain.

### Intent 1: Look up land record

- **Trigger phrases**: "Look up land record", "I need to look up land record", "Help me look up land record"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Look up land record
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Map land parcel

- **Trigger phrases**: "Map land parcel", "I need to map land parcel", "Help me map land parcel"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Map land parcel
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Check zoning

- **Trigger phrases**: "Check zoning", "I need to check zoning", "Help me check zoning"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check zoning
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Monitor environment

- **Trigger phrases**: "Monitor environment", "I need to monitor environment", "Help me monitor environment"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Monitor environment
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Process permit

- **Trigger phrases**: "Process permit", "I need to process permit", "Help me process permit"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Process permit
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Manage title

- **Trigger phrases**: "Manage title", "I need to manage title", "Help me manage title"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage title
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

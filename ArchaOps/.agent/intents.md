# 🏺 Archaeological Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Archaeological Operations domain.

### Intent 1: Log new artifact find

- **Trigger phrases**: "Log new artifact find", "I need to log new artifact find", "Help me log new artifact find"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Log new artifact find
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Map excavation site

- **Trigger phrases**: "Map excavation site", "I need to map excavation site", "Help me map excavation site"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Map excavation site
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Classify artifact by image

- **Trigger phrases**: "Classify artifact by image", "I need to classify artifact by image", "Help me classify artifact by image"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Classify artifact by image
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Check heritage compliance

- **Trigger phrases**: "Check heritage compliance", "I need to check heritage compliance", "Help me check heritage compliance"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check heritage compliance
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Export site data

- **Trigger phrases**: "Export site data", "I need to export site data", "Help me export site data"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Export site data
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Generate excavation report

- **Trigger phrases**: "Generate excavation report", "I need to generate excavation report", "Help me generate excavation report"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Generate excavation report
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

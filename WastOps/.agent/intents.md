# ♻️ Waste Management Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Waste Management Operations domain.

### Intent 1: Optimize collection route

- **Trigger phrases**: "Optimize collection route", "I need to optimize collection route", "Help me optimize collection route"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Optimize collection route
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Track recycling

- **Trigger phrases**: "Track recycling", "I need to track recycling", "Help me track recycling"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track recycling
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Check compliance

- **Trigger phrases**: "Check compliance", "I need to check compliance", "Help me check compliance"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check compliance
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Analyse waste data

- **Trigger phrases**: "Analyse waste data", "I need to analyse waste data", "Help me analyse waste data"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Analyse waste data
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Support circular economy

- **Trigger phrases**: "Support circular economy", "I need to support circular economy", "Help me support circular economy"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Support circular economy
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Monitor smart bins

- **Trigger phrases**: "Monitor smart bins", "I need to monitor smart bins", "Help me monitor smart bins"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Monitor smart bins
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

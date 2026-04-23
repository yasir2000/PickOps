# 🌾 Agricultural Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Agricultural Operations domain.

### Intent 1: Check soil moisture levels

- **Trigger phrases**: "Check soil moisture levels", "I need to check soil moisture levels", "Help me check soil moisture levels"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check soil moisture levels
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Plan irrigation schedule

- **Trigger phrases**: "Plan irrigation schedule", "I need to plan irrigation schedule", "Help me plan irrigation schedule"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Plan irrigation schedule
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Detect disease in crop images

- **Trigger phrases**: "Detect disease in crop images", "I need to detect disease in crop images", "Help me detect disease in crop images"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Detect disease in crop images
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Forecast this season's yield

- **Trigger phrases**: "Forecast this season's yield", "I need to forecast this season's yield", "Help me forecast this season's yield"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Forecast this season's yield
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Optimize fertilizer application

- **Trigger phrases**: "Optimize fertilizer application", "I need to optimize fertilizer application", "Help me optimize fertilizer application"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Optimize fertilizer application
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Track farm equipment

- **Trigger phrases**: "Track farm equipment", "I need to track farm equipment", "Help me track farm equipment"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track farm equipment
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

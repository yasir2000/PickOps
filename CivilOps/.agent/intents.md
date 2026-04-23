# 🏗️ Civil Engineering Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Civil Engineering Operations domain.

### Intent 1: Check bridge sensor data

- **Trigger phrases**: "Check bridge sensor data", "I need to check bridge sensor data", "Help me check bridge sensor data"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check bridge sensor data
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Update project schedule

- **Trigger phrases**: "Update project schedule", "I need to update project schedule", "Help me update project schedule"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Update project schedule
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Track road asset condition

- **Trigger phrases**: "Track road asset condition", "I need to track road asset condition", "Help me track road asset condition"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track road asset condition
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Generate GIS map

- **Trigger phrases**: "Generate GIS map", "I need to generate gis map", "Help me generate gis map"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Generate GIS map
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Assess environmental impact

- **Trigger phrases**: "Assess environmental impact", "I need to assess environmental impact", "Help me assess environmental impact"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Assess environmental impact
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Audit compliance status

- **Trigger phrases**: "Audit compliance status", "I need to audit compliance status", "Help me audit compliance status"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Audit compliance status
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

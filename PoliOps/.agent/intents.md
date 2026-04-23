# 🗳️ Political Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Political Operations domain.

### Intent 1: Automate voter outreach

- **Trigger phrases**: "Automate voter outreach", "I need to automate voter outreach", "Help me automate voter outreach"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Automate voter outreach
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Track donation

- **Trigger phrases**: "Track donation", "I need to track donation", "Help me track donation"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track donation
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Analyse campaign

- **Trigger phrases**: "Analyse campaign", "I need to analyse campaign", "Help me analyse campaign"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Analyse campaign
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Generate compliance report

- **Trigger phrases**: "Generate compliance report", "I need to generate compliance report", "Help me generate compliance report"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Generate compliance report
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Manage social media

- **Trigger phrases**: "Manage social media", "I need to manage social media", "Help me manage social media"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage social media
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Coordinate canvassing

- **Trigger phrases**: "Coordinate canvassing", "I need to coordinate canvassing", "Help me coordinate canvassing"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Coordinate canvassing
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

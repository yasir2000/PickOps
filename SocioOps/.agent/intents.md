# 🌍 Social Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Social Operations domain.

### Intent 1: Manage community

- **Trigger phrases**: "Manage community", "I need to manage community", "Help me manage community"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage community
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Track grant

- **Trigger phrases**: "Track grant", "I need to track grant", "Help me track grant"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track grant
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Measure impact

- **Trigger phrases**: "Measure impact", "I need to measure impact", "Help me measure impact"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Measure impact
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Coordinate volunteers

- **Trigger phrases**: "Coordinate volunteers", "I need to coordinate volunteers", "Help me coordinate volunteers"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Coordinate volunteers
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

### Intent 6: Generate impact report

- **Trigger phrases**: "Generate impact report", "I need to generate impact report", "Help me generate impact report"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Generate impact report
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

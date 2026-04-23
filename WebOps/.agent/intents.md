# 🌐 Web Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Web Operations domain.

### Intent 1: Manage CDN

- **Trigger phrases**: "Manage CDN", "I need to manage cdn", "Help me manage cdn"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage CDN
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Optimize performance

- **Trigger phrases**: "Optimize performance", "I need to optimize performance", "Help me optimize performance"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Optimize performance
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Enforce security

- **Trigger phrases**: "Enforce security", "I need to enforce security", "Help me enforce security"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Enforce security
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Deploy to edge

- **Trigger phrases**: "Deploy to edge", "I need to deploy to edge", "Help me deploy to edge"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Deploy to edge
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Monitor SEO

- **Trigger phrases**: "Monitor SEO", "I need to monitor seo", "Help me monitor seo"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Monitor SEO
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Audit accessibility

- **Trigger phrases**: "Audit accessibility", "I need to audit accessibility", "Help me audit accessibility"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Audit accessibility
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

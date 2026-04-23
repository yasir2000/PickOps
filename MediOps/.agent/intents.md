# 📰 Media Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Media Operations domain.

### Intent 1: Manage content production

- **Trigger phrases**: "Manage content production", "I need to manage content production", "Help me manage content production"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage content production
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Store digital asset

- **Trigger phrases**: "Store digital asset", "I need to store digital asset", "Help me store digital asset"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Store digital asset
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Publish content

- **Trigger phrases**: "Publish content", "I need to publish content", "Help me publish content"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Publish content
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Optimize for SEO

- **Trigger phrases**: "Optimize for SEO", "I need to optimize for seo", "Help me optimize for seo"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Optimize for SEO
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Analyse audience

- **Trigger phrases**: "Analyse audience", "I need to analyse audience", "Help me analyse audience"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Analyse audience
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Manage rights

- **Trigger phrases**: "Manage rights", "I need to manage rights", "Help me manage rights"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage rights
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

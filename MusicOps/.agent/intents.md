# 🎵 Music Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Music Operations domain.

### Intent 1: Submit music for distribution

- **Trigger phrases**: "Submit music for distribution", "I need to submit music for distribution", "Help me submit music for distribution"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Submit music for distribution
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Track royalties

- **Trigger phrases**: "Track royalties", "I need to track royalties", "Help me track royalties"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track royalties
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Analyse streaming performance

- **Trigger phrases**: "Analyse streaming performance", "I need to analyse streaming performance", "Help me analyse streaming performance"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Analyse streaming performance
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Manage track metadata

- **Trigger phrases**: "Manage track metadata", "I need to manage track metadata", "Help me manage track metadata"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage track metadata
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Optimize playlist

- **Trigger phrases**: "Optimize playlist", "I need to optimize playlist", "Help me optimize playlist"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Optimize playlist
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Register rights

- **Trigger phrases**: "Register rights", "I need to register rights", "Help me register rights"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Register rights
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

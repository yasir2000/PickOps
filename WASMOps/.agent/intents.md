# 🕸️ WebAssembly Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the WebAssembly Operations domain.

### Intent 1: Deploy WASM module

- **Trigger phrases**: "Deploy WASM module", "I need to deploy wasm module", "Help me deploy wasm module"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Deploy WASM module
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Manage module registry

- **Trigger phrases**: "Manage module registry", "I need to manage module registry", "Help me manage module registry"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage module registry
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Operate WASI runtime

- **Trigger phrases**: "Operate WASI runtime", "I need to operate wasi runtime", "Help me operate wasi runtime"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Operate WASI runtime
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Profile performance

- **Trigger phrases**: "Profile performance", "I need to profile performance", "Help me profile performance"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Profile performance
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Enforce sandbox

- **Trigger phrases**: "Enforce sandbox", "I need to enforce sandbox", "Help me enforce sandbox"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Enforce sandbox
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Manage component model

- **Trigger phrases**: "Manage component model", "I need to manage component model", "Help me manage component model"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage component model
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

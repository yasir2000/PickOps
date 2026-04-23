# ⛓️ Blockchain Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Blockchain Operations domain.

### Intent 1: Deploy smart contract

- **Trigger phrases**: "Deploy smart contract", "I need to deploy smart contract", "Help me deploy smart contract"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Deploy smart contract
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Monitor on-chain events

- **Trigger phrases**: "Monitor on-chain events", "I need to monitor on-chain events", "Help me monitor on-chain events"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Monitor on-chain events
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Check node health

- **Trigger phrases**: "Check node health", "I need to check node health", "Help me check node health"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check node health
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Transfer assets

- **Trigger phrases**: "Transfer assets", "I need to transfer assets", "Help me transfer assets"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Transfer assets
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Interact with DeFi protocol

- **Trigger phrases**: "Interact with DeFi protocol", "I need to interact with defi protocol", "Help me interact with defi protocol"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Interact with DeFi protocol
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Bridge tokens to L2

- **Trigger phrases**: "Bridge tokens to L2", "I need to bridge tokens to l2", "Help me bridge tokens to l2"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Bridge tokens to L2
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

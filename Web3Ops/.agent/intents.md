# 🌐 Web3 Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Web3 Operations domain.

### Intent 1: Operate DeFi protocol

- **Trigger phrases**: "Operate DeFi protocol", "I need to operate defi protocol", "Help me operate defi protocol"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Operate DeFi protocol
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Manage NFT platform

- **Trigger phrases**: "Manage NFT platform", "I need to manage nft platform", "Help me manage nft platform"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage NFT platform
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Run DAO governance

- **Trigger phrases**: "Run DAO governance", "I need to run dao governance", "Help me run dao governance"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Run DAO governance
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Manage node

- **Trigger phrases**: "Manage node", "I need to manage node", "Help me manage node"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage node
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Monitor smart contract

- **Trigger phrases**: "Monitor smart contract", "I need to monitor smart contract", "Help me monitor smart contract"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Monitor smart contract
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Bridge cross-chain

- **Trigger phrases**: "Bridge cross-chain", "I need to bridge cross-chain", "Help me bridge cross-chain"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Bridge cross-chain
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

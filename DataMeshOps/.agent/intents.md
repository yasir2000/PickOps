# 🕸️ Data Mesh Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Data Mesh Operations domain.

### Intent 1: Register data product

- **Trigger phrases**: "Register data product", "I need to register data product", "Help me register data product"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Register data product
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Enforce data contract

- **Trigger phrases**: "Enforce data contract", "I need to enforce data contract", "Help me enforce data contract"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Enforce data contract
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Check data quality

- **Trigger phrases**: "Check data quality", "I need to check data quality", "Help me check data quality"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check data quality
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Manage domain access

- **Trigger phrases**: "Manage domain access", "I need to manage domain access", "Help me manage domain access"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage domain access
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Track data lineage

- **Trigger phrases**: "Track data lineage", "I need to track data lineage", "Help me track data lineage"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track data lineage
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Alert on SLA breach

- **Trigger phrases**: "Alert on SLA breach", "I need to alert on sla breach", "Help me alert on sla breach"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Alert on SLA breach
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

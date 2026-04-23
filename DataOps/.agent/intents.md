# 📊 Data Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Data Operations domain.

### Intent 1: Build data pipeline

- **Trigger phrases**: "Build data pipeline", "I need to build data pipeline", "Help me build data pipeline"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Build data pipeline
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Validate data quality

- **Trigger phrases**: "Validate data quality", "I need to validate data quality", "Help me validate data quality"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Validate data quality
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Update data catalog

- **Trigger phrases**: "Update data catalog", "I need to update data catalog", "Help me update data catalog"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Update data catalog
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Run ETL job

- **Trigger phrases**: "Run ETL job", "I need to run etl job", "Help me run etl job"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Run ETL job
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Track lineage

- **Trigger phrases**: "Track lineage", "I need to track lineage", "Help me track lineage"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Track lineage
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Deliver analytics report

- **Trigger phrases**: "Deliver analytics report", "I need to deliver analytics report", "Help me deliver analytics report"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Deliver analytics report
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

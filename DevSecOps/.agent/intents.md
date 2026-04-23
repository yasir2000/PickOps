# 🔒 Development Security Operations Agent — Intents

## Supported Intents

This agent handles **6 primary intents** in the Development Security Operations domain.

### Intent 1: Scan code for vulnerabilities

- **Trigger phrases**: "Scan code for vulnerabilities", "I need to scan code for vulnerabilities", "Help me scan code for vulnerabilities"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Scan code for vulnerabilities
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 2: Check container image CVEs

- **Trigger phrases**: "Check container image CVEs", "I need to check container image cves", "Help me check container image cves"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Check container image CVEs
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 3: Detect secrets in repo

- **Trigger phrases**: "Detect secrets in repo", "I need to detect secrets in repo", "Help me detect secrets in repo"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Detect secrets in repo
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 4: Generate SBOM

- **Trigger phrases**: "Generate SBOM", "I need to generate sbom", "Help me generate sbom"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Generate SBOM
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 5: Enforce security policy

- **Trigger phrases**: "Enforce security policy", "I need to enforce security policy", "Help me enforce security policy"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Enforce security policy
  Agent: I'll handle that for you. [Executes relevant tools and returns result]
  ```

### Intent 6: Manage vulnerability backlog

- **Trigger phrases**: "Manage vulnerability backlog", "I need to manage vulnerability backlog", "Help me manage vulnerability backlog"
- **Required slots**: context-dependent
- **Response type**: Structured result with actions taken
- **Example**:
  ```
  User: Manage vulnerability backlog
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

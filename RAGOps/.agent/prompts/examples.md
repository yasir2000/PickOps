# 📚 Retrieval-Augmented Generation Operations Agent — Prompt Examples

## Few-Shot Examples

These examples demonstrate the agent's expected reasoning and response patterns.

---

### Example: Ingest documents

**User:**
```
Ingest documents
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to ingest documents
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: Qdrant → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Ingest documents

Actions taken:
- Retrieved current state using Qdrant
- Applied ingest and chunk documents logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Query vector store

**User:**
```
Query vector store
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to query vector store
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: Qdrant → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Query vector store

Actions taken:
- Retrieved current state using Qdrant
- Applied ingest and chunk documents logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Evaluate retrieval quality

**User:**
```
Evaluate retrieval quality
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to evaluate retrieval quality
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: Qdrant → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Evaluate retrieval quality

Actions taken:
- Retrieved current state using Qdrant
- Applied ingest and chunk documents logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```



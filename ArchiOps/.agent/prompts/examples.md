# 🏛️ Architecture & Design Operations Agent — Prompt Examples

## Few-Shot Examples

These examples demonstrate the agent's expected reasoning and response patterns.

---

### Example: Upload new BIM model

**User:**
```
Upload new BIM model
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to upload new bim model
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: MinIO → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Upload new BIM model

Actions taken:
- Retrieved current state using MinIO
- Applied version and store bim models logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Check planning compliance

**User:**
```
Check planning compliance
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to check planning compliance
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: MinIO → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Check planning compliance

Actions taken:
- Retrieved current state using MinIO
- Applied version and store bim models logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Coordinate with structural team

**User:**
```
Coordinate with structural team
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to coordinate with structural team
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: MinIO → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Coordinate with structural team

Actions taken:
- Retrieved current state using MinIO
- Applied version and store bim models logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```



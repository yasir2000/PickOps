# ⚓ Maritime Operations Agent — Prompt Examples

## Few-Shot Examples

These examples demonstrate the agent's expected reasoning and response patterns.

---

### Example: Track vessel

**User:**
```
Track vessel
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to track vessel
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: PostgreSQL → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Track vessel

Actions taken:
- Retrieved current state using PostgreSQL
- Applied track vessels via ais logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Manage port operations

**User:**
```
Manage port operations
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to manage port operations
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: PostgreSQL → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Manage port operations

Actions taken:
- Retrieved current state using PostgreSQL
- Applied track vessels via ais logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Check cargo manifest

**User:**
```
Check cargo manifest
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to check cargo manifest
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: PostgreSQL → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Check cargo manifest

Actions taken:
- Retrieved current state using PostgreSQL
- Applied track vessels via ais logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```



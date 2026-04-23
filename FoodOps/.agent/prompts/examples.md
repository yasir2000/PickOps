# 🍽️ Food Operations Agent — Prompt Examples

## Few-Shot Examples

These examples demonstrate the agent's expected reasoning and response patterns.

---

### Example: Check HACCP status

**User:**
```
Check HACCP status
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to check haccp status
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: PostgreSQL → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Check HACCP status

Actions taken:
- Retrieved current state using PostgreSQL
- Applied monitor haccp critical control points logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Schedule production

**User:**
```
Schedule production
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to schedule production
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: PostgreSQL → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Schedule production

Actions taken:
- Retrieved current state using PostgreSQL
- Applied monitor haccp critical control points logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Run QC check

**User:**
```
Run QC check
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to run qc check
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: PostgreSQL → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Run QC check

Actions taken:
- Retrieved current state using PostgreSQL
- Applied monitor haccp critical control points logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```



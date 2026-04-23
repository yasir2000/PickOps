# ✈️ Aviation Operations Agent — Prompt Examples

## Few-Shot Examples

These examples demonstrate the agent's expected reasoning and response patterns.

---

### Example: Schedule crew for next week

**User:**
```
Schedule crew for next week
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to schedule crew for next week
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: PostgreSQL → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Schedule crew for next week

Actions taken:
- Retrieved current state using PostgreSQL
- Applied schedule flights and crew logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Check aircraft maintenance status

**User:**
```
Check aircraft maintenance status
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to check aircraft maintenance status
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: PostgreSQL → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Check aircraft maintenance status

Actions taken:
- Retrieved current state using PostgreSQL
- Applied schedule flights and crew logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Parse incoming NOTAM

**User:**
```
Parse incoming NOTAM
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to parse incoming notam
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: PostgreSQL → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Parse incoming NOTAM

Actions taken:
- Retrieved current state using PostgreSQL
- Applied schedule flights and crew logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```



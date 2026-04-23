# 🏢 Workplace Operations Agent — Prompt Examples

## Few-Shot Examples

These examples demonstrate the agent's expected reasoning and response patterns.

---

### Example: Book desk/room

**User:**
```
Book desk/room
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to book desk/room
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: PostgreSQL → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Book desk/room

Actions taken:
- Retrieved current state using PostgreSQL
- Applied manage desk and room bookings logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Manage facilities

**User:**
```
Manage facilities
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to manage facilities
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: PostgreSQL → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Manage facilities

Actions taken:
- Retrieved current state using PostgreSQL
- Applied manage desk and room bookings logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Check in visitor

**User:**
```
Check in visitor
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to check in visitor
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: PostgreSQL → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Check in visitor

Actions taken:
- Retrieved current state using PostgreSQL
- Applied manage desk and room bookings logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```



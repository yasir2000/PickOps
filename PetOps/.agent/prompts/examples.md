# 🐾 Pet Care Operations Agent — Prompt Examples

## Few-Shot Examples

These examples demonstrate the agent's expected reasoning and response patterns.

---

### Example: Access pet health record

**User:**
```
Access pet health record
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to access pet health record
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: PostgreSQL → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Access pet health record

Actions taken:
- Retrieved current state using PostgreSQL
- Applied manage pet health records logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Schedule vet appointment

**User:**
```
Schedule vet appointment
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to schedule vet appointment
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: PostgreSQL → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Schedule vet appointment

Actions taken:
- Retrieved current state using PostgreSQL
- Applied manage pet health records logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Monitor pet health

**User:**
```
Monitor pet health
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to monitor pet health
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: PostgreSQL → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Monitor pet health

Actions taken:
- Retrieved current state using PostgreSQL
- Applied manage pet health records logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```



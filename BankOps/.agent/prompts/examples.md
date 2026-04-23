# 🏦 Banking Operations Agent — Prompt Examples

## Few-Shot Examples

These examples demonstrate the agent's expected reasoning and response patterns.

---

### Example: Process payment

**User:**
```
Process payment
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to process payment
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: PostgreSQL → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Process payment

Actions taken:
- Retrieved current state using PostgreSQL
- Applied process swift/ach payments logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Flag suspicious transaction

**User:**
```
Flag suspicious transaction
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to flag suspicious transaction
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: PostgreSQL → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Flag suspicious transaction

Actions taken:
- Retrieved current state using PostgreSQL
- Applied process swift/ach payments logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Run KYC check

**User:**
```
Run KYC check
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to run kyc check
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: PostgreSQL → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Run KYC check

Actions taken:
- Retrieved current state using PostgreSQL
- Applied process swift/ach payments logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```



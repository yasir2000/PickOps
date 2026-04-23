# 🐄 Dairy Operations Agent — Prompt Examples

## Few-Shot Examples

These examples demonstrate the agent's expected reasoning and response patterns.

---

### Example: Check herd health

**User:**
```
Check herd health
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to check herd health
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: MQTT → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Check herd health

Actions taken:
- Retrieved current state using MQTT
- Applied monitor herd health sensors logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Schedule milking

**User:**
```
Schedule milking
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to schedule milking
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: MQTT → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Schedule milking

Actions taken:
- Retrieved current state using MQTT
- Applied monitor herd health sensors logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Log milk quality

**User:**
```
Log milk quality
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to log milk quality
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: MQTT → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Log milk quality

Actions taken:
- Retrieved current state using MQTT
- Applied monitor herd health sensors logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```



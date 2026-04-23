# 👴 Elder Care Operations Agent — Prompt Examples

## Few-Shot Examples

These examples demonstrate the agent's expected reasoning and response patterns.

---

### Example: Monitor resident health

**User:**
```
Monitor resident health
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to monitor resident health
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: MQTT → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Monitor resident health

Actions taken:
- Retrieved current state using MQTT
- Applied monitor resident health sensors logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Schedule medication

**User:**
```
Schedule medication
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to schedule medication
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: MQTT → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Schedule medication

Actions taken:
- Retrieved current state using MQTT
- Applied monitor resident health sensors logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Detect fall event

**User:**
```
Detect fall event
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to detect fall event
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: MQTT → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Detect fall event

Actions taken:
- Retrieved current state using MQTT
- Applied monitor resident health sensors logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```



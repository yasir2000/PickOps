# 🐔 Poultry Operations Agent — Prompt Examples

## Few-Shot Examples

These examples demonstrate the agent's expected reasoning and response patterns.

---

### Example: Monitor flock health

**User:**
```
Monitor flock health
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to monitor flock health
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: MQTT → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Monitor flock health

Actions taken:
- Retrieved current state using MQTT
- Applied monitor flock health sensors logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Manage feed

**User:**
```
Manage feed
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to manage feed
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: MQTT → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Manage feed

Actions taken:
- Retrieved current state using MQTT
- Applied monitor flock health sensors logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Enforce biosecurity

**User:**
```
Enforce biosecurity
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to enforce biosecurity
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: MQTT → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Enforce biosecurity

Actions taken:
- Retrieved current state using MQTT
- Applied monitor flock health sensors logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```



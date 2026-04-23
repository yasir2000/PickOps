# ⚗️ Chemical Operations Agent — Prompt Examples

## Few-Shot Examples

These examples demonstrate the agent's expected reasoning and response patterns.

---

### Example: Check process parameters

**User:**
```
Check process parameters
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to check process parameters
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: MQTT → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Check process parameters

Actions taken:
- Retrieved current state using MQTT
- Applied monitor process parameters logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Alert on safety breach

**User:**
```
Alert on safety breach
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to alert on safety breach
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: MQTT → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Alert on safety breach

Actions taken:
- Retrieved current state using MQTT
- Applied monitor process parameters logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Check chemical stock

**User:**
```
Check chemical stock
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to check chemical stock
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: MQTT → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Check chemical stock

Actions taken:
- Retrieved current state using MQTT
- Applied monitor process parameters logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```



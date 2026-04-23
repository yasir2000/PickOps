# 🌾 Agricultural Operations Agent — Prompt Examples

## Few-Shot Examples

These examples demonstrate the agent's expected reasoning and response patterns.

---

### Example: Check soil moisture levels

**User:**
```
Check soil moisture levels
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to check soil moisture levels
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: MQTT → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Check soil moisture levels

Actions taken:
- Retrieved current state using MQTT
- Applied monitor soil sensors logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Plan irrigation schedule

**User:**
```
Plan irrigation schedule
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to plan irrigation schedule
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: MQTT → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Plan irrigation schedule

Actions taken:
- Retrieved current state using MQTT
- Applied monitor soil sensors logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Detect disease in crop images

**User:**
```
Detect disease in crop images
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to detect disease in crop images
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: MQTT → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Detect disease in crop images

Actions taken:
- Retrieved current state using MQTT
- Applied monitor soil sensors logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```



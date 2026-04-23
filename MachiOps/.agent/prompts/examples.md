# ⚙️ Machinery Operations Agent — Prompt Examples

## Few-Shot Examples

These examples demonstrate the agent's expected reasoning and response patterns.

---

### Example: Monitor machine health

**User:**
```
Monitor machine health
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to monitor machine health
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: MQTT → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Monitor machine health

Actions taken:
- Retrieved current state using MQTT
- Applied monitor machinery sensors logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Predict failure

**User:**
```
Predict failure
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to predict failure
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: MQTT → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Predict failure

Actions taken:
- Retrieved current state using MQTT
- Applied monitor machinery sensors logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Manage equipment lifecycle

**User:**
```
Manage equipment lifecycle
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to manage equipment lifecycle
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: MQTT → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Manage equipment lifecycle

Actions taken:
- Retrieved current state using MQTT
- Applied monitor machinery sensors logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```



# ⚡ Energy Operations Agent — Prompt Examples

## Few-Shot Examples

These examples demonstrate the agent's expected reasoning and response patterns.

---

### Example: Check grid status

**User:**
```
Check grid status
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to check grid status
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: MQTT → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Check grid status

Actions taken:
- Retrieved current state using MQTT
- Applied monitor grid health in real time logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Dispatch renewable energy

**User:**
```
Dispatch renewable energy
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to dispatch renewable energy
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: MQTT → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Dispatch renewable energy

Actions taken:
- Retrieved current state using MQTT
- Applied monitor grid health in real time logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Forecast demand

**User:**
```
Forecast demand
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to forecast demand
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: MQTT → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Forecast demand

Actions taken:
- Retrieved current state using MQTT
- Applied monitor grid health in real time logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```



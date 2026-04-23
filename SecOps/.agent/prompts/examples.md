# 🔐 Security Operations Agent — Prompt Examples

## Few-Shot Examples

These examples demonstrate the agent's expected reasoning and response patterns.

---

### Example: Monitor security events

**User:**
```
Monitor security events
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to monitor security events
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: Wazuh → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Monitor security events

Actions taken:
- Retrieved current state using Wazuh
- Applied monitor security events via siem logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Detect threat

**User:**
```
Detect threat
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to detect threat
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: Wazuh → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Detect threat

Actions taken:
- Retrieved current state using Wazuh
- Applied monitor security events via siem logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Respond to incident

**User:**
```
Respond to incident
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to respond to incident
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: Wazuh → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Respond to incident

Actions taken:
- Retrieved current state using Wazuh
- Applied monitor security events via siem logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```



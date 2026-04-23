# 📱 Application Operations Agent — Prompt Examples

## Few-Shot Examples

These examples demonstrate the agent's expected reasoning and response patterns.

---

### Example: Deploy new version

**User:**
```
Deploy new version
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to deploy new version
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: LaunchDarkly → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Deploy new version

Actions taken:
- Retrieved current state using LaunchDarkly
- Applied deploy applications with zero downtime logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Toggle feature flag

**User:**
```
Toggle feature flag
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to toggle feature flag
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: LaunchDarkly → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Toggle feature flag

Actions taken:
- Retrieved current state using LaunchDarkly
- Applied deploy applications with zero downtime logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Investigate error spike

**User:**
```
Investigate error spike
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to investigate error spike
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: LaunchDarkly → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Investigate error spike

Actions taken:
- Retrieved current state using LaunchDarkly
- Applied deploy applications with zero downtime logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```



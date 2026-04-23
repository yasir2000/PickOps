# ☁️ AWS Cloud Operations Agent — Prompt Examples

## Few-Shot Examples

These examples demonstrate the agent's expected reasoning and response patterns.

---

### Example: Provision new environment

**User:**
```
Provision new environment
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to provision new environment
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: AWS → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Provision new environment

Actions taken:
- Retrieved current state using AWS
- Applied provision resources via cloudformation/cdk logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Find cost anomalies

**User:**
```
Find cost anomalies
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to find cost anomalies
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: AWS → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Find cost anomalies

Actions taken:
- Retrieved current state using AWS
- Applied provision resources via cloudformation/cdk logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Check security posture

**User:**
```
Check security posture
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to check security posture
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: AWS → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Check security posture

Actions taken:
- Retrieved current state using AWS
- Applied provision resources via cloudformation/cdk logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```



# 🔷 Azure Cloud Operations Agent — Prompt Examples

## Few-Shot Examples

These examples demonstrate the agent's expected reasoning and response patterns.

---

### Example: Deploy Azure resource

**User:**
```
Deploy Azure resource
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to deploy azure resource
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: Azure → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Deploy Azure resource

Actions taken:
- Retrieved current state using Azure
- Applied deploy arm/bicep templates logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Enforce governance policy

**User:**
```
Enforce governance policy
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to enforce governance policy
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: Azure → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Enforce governance policy

Actions taken:
- Retrieved current state using Azure
- Applied deploy arm/bicep templates logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Check budget status

**User:**
```
Check budget status
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to check budget status
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: Azure → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Check budget status

Actions taken:
- Retrieved current state using Azure
- Applied deploy arm/bicep templates logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```



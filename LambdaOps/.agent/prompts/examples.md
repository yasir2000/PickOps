# λ Serverless Lambda Operations Agent — Prompt Examples

## Few-Shot Examples

These examples demonstrate the agent's expected reasoning and response patterns.

---

### Example: Deploy serverless function

**User:**
```
Deploy serverless function
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to deploy serverless function
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: AWS → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Deploy serverless function

Actions taken:
- Retrieved current state using AWS
- Applied deploy and version serverless functions logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Reduce cold starts

**User:**
```
Reduce cold starts
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to reduce cold starts
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: AWS → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Reduce cold starts

Actions taken:
- Retrieved current state using AWS
- Applied deploy and version serverless functions logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Monitor function metrics

**User:**
```
Monitor function metrics
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to monitor function metrics
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: AWS → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Monitor function metrics

Actions taken:
- Retrieved current state using AWS
- Applied deploy and version serverless functions logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```



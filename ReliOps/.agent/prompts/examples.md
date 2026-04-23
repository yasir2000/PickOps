# 🔋 Reliability Operations Agent — Prompt Examples

## Few-Shot Examples

These examples demonstrate the agent's expected reasoning and response patterns.

---

### Example: Define SLO

**User:**
```
Define SLO
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to define slo
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: Prometheus → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Define SLO

Actions taken:
- Retrieved current state using Prometheus
- Applied define and track slos logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Check error budget

**User:**
```
Check error budget
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to check error budget
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: Prometheus → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Check error budget

Actions taken:
- Retrieved current state using Prometheus
- Applied define and track slos logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Run reliability test

**User:**
```
Run reliability test
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to run reliability test
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: Prometheus → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Run reliability test

Actions taken:
- Retrieved current state using Prometheus
- Applied define and track slos logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```



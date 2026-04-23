# 🤖 Machine Learning Operations Agent — Prompt Examples

## Few-Shot Examples

These examples demonstrate the agent's expected reasoning and response patterns.

---

### Example: Train ML model

**User:**
```
Train ML model
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to train ml model
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: MLflow → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Train ML model

Actions taken:
- Retrieved current state using MLflow
- Applied build and run training pipelines logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Register model version

**User:**
```
Register model version
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to register model version
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: MLflow → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Register model version

Actions taken:
- Retrieved current state using MLflow
- Applied build and run training pipelines logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Deploy model endpoint

**User:**
```
Deploy model endpoint
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to deploy model endpoint
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: MLflow → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Deploy model endpoint

Actions taken:
- Retrieved current state using MLflow
- Applied build and run training pipelines logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```



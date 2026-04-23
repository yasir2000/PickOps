# 🧬 Large Language Model Operations Agent — Prompt Examples

## Few-Shot Examples

These examples demonstrate the agent's expected reasoning and response patterns.

---

### Example: Deploy LLM endpoint

**User:**
```
Deploy LLM endpoint
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to deploy llm endpoint
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: vLLM → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Deploy LLM endpoint

Actions taken:
- Retrieved current state using vLLM
- Applied serve and scale llms logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Run fine-tuning job

**User:**
```
Run fine-tuning job
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to run fine-tuning job
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: vLLM → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Run fine-tuning job

Actions taken:
- Retrieved current state using vLLM
- Applied serve and scale llms logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Evaluate model

**User:**
```
Evaluate model
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to evaluate model
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: vLLM → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Evaluate model

Actions taken:
- Retrieved current state using vLLM
- Applied serve and scale llms logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```



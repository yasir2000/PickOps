# 📚 Publishing Operations Agent — Prompt Examples

## Few-Shot Examples

These examples demonstrate the agent's expected reasoning and response patterns.

---

### Example: Submit manuscript

**User:**
```
Submit manuscript
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to submit manuscript
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: PostgreSQL → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Submit manuscript

Actions taken:
- Retrieved current state using PostgreSQL
- Applied manage manuscript submissions logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Run editorial review

**User:**
```
Run editorial review
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to run editorial review
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: PostgreSQL → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Run editorial review

Actions taken:
- Retrieved current state using PostgreSQL
- Applied manage manuscript submissions logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Manage production

**User:**
```
Manage production
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to manage production
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: PostgreSQL → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Manage production

Actions taken:
- Retrieved current state using PostgreSQL
- Applied manage manuscript submissions logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```



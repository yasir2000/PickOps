# 🛩️ Avionics Operations Agent — Prompt Examples

## Few-Shot Examples

These examples demonstrate the agent's expected reasoning and response patterns.

---

### Example: Run avionics test suite

**User:**
```
Run avionics test suite
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to run avionics test suite
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: LDRA → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Run avionics test suite

Actions taken:
- Retrieved current state using LDRA
- Applied run avionics software tests logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Check DO-178C compliance

**User:**
```
Check DO-178C compliance
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to check do-178c compliance
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: LDRA → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Check DO-178C compliance

Actions taken:
- Retrieved current state using LDRA
- Applied run avionics software tests logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Push firmware update

**User:**
```
Push firmware update
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to push firmware update
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: LDRA → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Push firmware update

Actions taken:
- Retrieved current state using LDRA
- Applied run avionics software tests logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```



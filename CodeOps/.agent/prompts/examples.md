# 💻 Code Operations Agent — Prompt Examples

## Few-Shot Examples

These examples demonstrate the agent's expected reasoning and response patterns.

---

### Example: Analyse code quality

**User:**
```
Analyse code quality
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to analyse code quality
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: SonarQube → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Analyse code quality

Actions taken:
- Retrieved current state using SonarQube
- Applied run static analysis on prs logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Scan for vulnerable dependencies

**User:**
```
Scan for vulnerable dependencies
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to scan for vulnerable dependencies
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: SonarQube → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Scan for vulnerable dependencies

Actions taken:
- Retrieved current state using SonarQube
- Applied run static analysis on prs logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Review PR automatically

**User:**
```
Review PR automatically
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to review pr automatically
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: SonarQube → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Review PR automatically

Actions taken:
- Retrieved current state using SonarQube
- Applied run static analysis on prs logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```



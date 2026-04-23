# 🔒 Development Security Operations Agent — Prompt Examples

## Few-Shot Examples

These examples demonstrate the agent's expected reasoning and response patterns.

---

### Example: Scan code for vulnerabilities

**User:**
```
Scan code for vulnerabilities
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to scan code for vulnerabilities
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: Semgrep → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Scan code for vulnerabilities

Actions taken:
- Retrieved current state using Semgrep
- Applied run sast in ci pipelines logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Check container image CVEs

**User:**
```
Check container image CVEs
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to check container image cves
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: Semgrep → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Check container image CVEs

Actions taken:
- Retrieved current state using Semgrep
- Applied run sast in ci pipelines logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Detect secrets in repo

**User:**
```
Detect secrets in repo
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to detect secrets in repo
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: Semgrep → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Detect secrets in repo

Actions taken:
- Retrieved current state using Semgrep
- Applied run sast in ci pipelines logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```



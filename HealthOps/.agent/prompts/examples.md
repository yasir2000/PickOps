# 🏥 Healthcare Operations Agent — Prompt Examples

## Few-Shot Examples

These examples demonstrate the agent's expected reasoning and response patterns.

---

### Example: Access patient record

**User:**
```
Access patient record
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to access patient record
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: HL7 → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Access patient record

Actions taken:
- Retrieved current state using HL7
- Applied manage patient records via fhir logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Document clinical note

**User:**
```
Document clinical note
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to document clinical note
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: HL7 → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Document clinical note

Actions taken:
- Retrieved current state using HL7
- Applied manage patient records via fhir logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Check HIPAA compliance

**User:**
```
Check HIPAA compliance
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to check hipaa compliance
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: HL7 → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Check HIPAA compliance

Actions taken:
- Retrieved current state using HL7
- Applied manage patient records via fhir logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```



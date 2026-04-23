# 🗺️ Land Management Operations Agent — Prompt Examples

## Few-Shot Examples

These examples demonstrate the agent's expected reasoning and response patterns.

---

### Example: Look up land record

**User:**
```
Look up land record
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to look up land record
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: PostgreSQL → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Look up land record

Actions taken:
- Retrieved current state using PostgreSQL
- Applied manage land parcel records logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Map land parcel

**User:**
```
Map land parcel
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to map land parcel
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: PostgreSQL → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Map land parcel

Actions taken:
- Retrieved current state using PostgreSQL
- Applied manage land parcel records logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```

---

### Example: Check zoning

**User:**
```
Check zoning
```

**Agent Reasoning (Chain-of-Thought):**
```
1. Understanding: User wants to check zoning
2. Plan: I need to use the appropriate tool to fulfill this request
3. Tool call: PostgreSQL → fetch relevant data
4. Validate: Check result is valid and complete
5. Respond: Return structured result with recommendations
```

**Agent Response:**
```
✅ Task completed: Check zoning

Actions taken:
- Retrieved current state using PostgreSQL
- Applied manage land parcel records logic
- Validated result against expected parameters

Result: [Domain-specific structured output]

Follow-up recommendations:
- Monitor the outcome for 30 minutes
- Review logs if anomalies are detected
```



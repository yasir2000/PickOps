# Jira Workflow Automation

Complete automation of Jira workflows using the Jira REST API.

## Features

- **Project Management**: Create projects and configure settings
- **Issue Creation**: Automated epic, story, and subtask creation
- **Workflow Automation**: Transition issues based on conditions
- **Reporting**: Generate comprehensive project reports
- **Daily Tasks**: Automate routine operations

## Setup

1. Start ALMOps stack:
```bash
cd ALMOps
docker-compose up -d jira postgres
```

2. Access Jira at http://localhost:8080

3. Set up Jira:
   - Complete initial setup wizard
   - Create API token: Profile → Security → API Tokens
   - Update credentials in `automate.py`

4. Install dependencies:
```bash
pip install jira
```

## Usage

### Basic Automation

```bash
python automate.py
```

This will:
- Create demo project
- Set up sprint workflow with epic, stories, subtasks
- Generate project report
- Run daily automation tasks

### Custom Workflows

```python
from automate import JiraAutomation

# Initialize
jira = JiraAutomation(
    server="http://localhost:8080",
    user="admin",
    token="your-token"
)

# Create epic
epic = jira.create_epic(
    summary="New Feature",
    description="Feature description"
)

# Create story
story = jira.create_story(
    summary="Implement API",
    description="REST API implementation",
    epic_key=epic,
    story_points=5
)

# Add subtasks
jira.create_subtask(story, "Design schema")
jira.create_subtask(story, "Implement endpoints")

# Transition
jira.transition_issue(story, "In Progress")

# Generate report
report = jira.generate_report()
```

## Automation Features

### Sprint Workflow
- Creates complete sprint structure
- Links dependencies
- Adds initial comments
- Sets story points

### Daily Automation
1. **Stale Issue Detection**: Finds issues with no updates in 7 days
2. **Auto-Close Stories**: Closes stories when all subtasks are done
3. **Project Reporting**: Generates daily statistics

### Reporting Metrics
- Total issue count
- Issues by type (Epic, Story, Task, Bug)
- Issues by status (To Do, In Progress, Done)
- Total story points

## Example Output

```
📋 Jira Workflow Automation
============================================================
📋 Creating project: Demo Project (DEMO)
✅ Project created: DEMO

🏃 Creating Sprint Workflow
============================================================
🎯 Creating epic: User Authentication System
   Created: DEMO-1
📖 Creating story: Login functionality
   Created: DEMO-2
   📌 Creating subtask: Design login UI
      Created: DEMO-3
   📌 Creating subtask: Implement backend API
      Created: DEMO-4
🔗 Linking DEMO-2 Blocks DEMO-5
💬 Added comment to DEMO-2
🔄 Transitioning DEMO-2 to In Progress
   ✅ Transitioned to In Progress

📊 Generating report for DEMO
============================================================
Total Issues: 8

By Type:
  Epic: 1
  Story: 3
  Sub-task: 4

By Status:
  To Do: 6
  In Progress: 1
  Done: 1

Total Story Points: 16

🤖 Running Daily Automation
============================================================
⚠️  Found 2 stale issues:
   DEMO-5: OAuth2 integration
   DEMO-6: Password reset flow
✅ All subtasks done for DEMO-2, transitioning to Done

✅ Daily automation complete!
```

## Advanced Usage

### Custom JQL Queries

```python
# Find high-priority bugs
bugs = jira.jira.search_issues(
    'project=DEMO AND issuetype=Bug AND priority=High'
)

# Find issues assigned to me
my_issues = jira.jira.search_issues(
    'assignee=currentUser() AND status != Done'
)

# Sprint burndown data
sprint_issues = jira.jira.search_issues(
    'project=DEMO AND sprint in openSprints()'
)
```

### Bulk Operations

```python
# Bulk update assignee
issues = jira.jira.search_issues('project=DEMO AND assignee is EMPTY')
for issue in issues:
    issue.update(assignee={'name': 'admin'})

# Bulk transition
for issue in issues:
    jira.transition_issue(issue.key, "In Progress")
```

### Webhooks Integration

```python
# Create webhook for CI/CD integration
webhook = jira.jira.create_webhook(
    name="Jenkins Integration",
    url="http://jenkins:8085/jira-webhook",
    events=["jira:issue_updated", "jira:issue_created"]
)
```

## Integration with ALMOps Stack

### GitLab Integration
```python
# Add GitLab branch reference
jira.add_comment(
    "DEMO-2",
    "Branch created: feature/DEMO-2-login\n"
    "http://localhost:8929/project/-/tree/feature/DEMO-2-login"
)
```

### Jenkins Integration
```python
# Update issue from Jenkins pipeline
jira.add_comment(
    issue_key,
    f"Build #{build_number} completed\n"
    f"Status: {build_status}\n"
    f"URL: {jenkins_url}"
)

if build_status == "SUCCESS":
    jira.transition_issue(issue_key, "Ready for QA")
```

### Confluence Integration
```python
# Link to documentation
jira.jira.create_remote_link(
    issue="DEMO-1",
    destination={
        'url': 'http://localhost:8090/display/DEMO/Architecture',
        'title': 'Architecture Documentation'
    }
)
```

## Troubleshooting

### Connection Issues
- Verify Jira is running: `docker-compose ps jira`
- Check logs: `docker-compose logs jira`
- Ensure API token is valid

### Permission Errors
- User must have project admin permissions
- Verify issue type schemes are configured
- Check workflow permissions

### Custom Fields
```python
# Find custom field IDs
all_fields = jira.jira.fields()
for field in all_fields:
    if 'story' in field['name'].lower():
        print(f"{field['name']}: {field['id']}")
```

## Resources

- [Jira REST API Docs](https://developer.atlassian.com/cloud/jira/platform/rest/v3/)
- [Python Jira Library](https://jira.readthedocs.io/)
- [ALMOps Documentation](../README.md)

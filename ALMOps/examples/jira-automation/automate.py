"""
Jira Workflow Automation
Demonstrates: Issue creation, transitions, automation, reporting
"""

from jira import JIRA
from datetime import datetime, timedelta
from typing import List, Dict, Any
import json

JIRA_SERVER = "http://localhost:8080"
JIRA_USER = "admin"
JIRA_TOKEN = "your-api-token"

class JiraAutomation:
    """Automate Jira workflows"""

    def __init__(self, server: str = JIRA_SERVER, user: str = JIRA_USER, token: str = JIRA_TOKEN):
        self.jira = JIRA(server=server, basic_auth=(user, token))
        self.project_key = "DEMO"

    def create_project(self, key: str, name: str, lead: str) -> Dict:
        """Create new Jira project"""

        print(f"📋 Creating project: {name} ({key})")

        try:
            project = self.jira.create_project(
                key=key,
                name=name,
                projectTypeKey='software',
                lead=lead,
                description=f"Project {name} for demonstration"
            )

            print(f"✅ Project created: {project.key}")
            return {"key": project.key, "name": project.name}

        except Exception as e:
            print(f"⚠️  Project may already exist: {str(e)}")
            return {"key": key, "name": name}

    def create_epic(self, summary: str, description: str) -> str:
        """Create epic"""

        print(f"🎯 Creating epic: {summary}")

        issue = self.jira.create_issue(
            project=self.project_key,
            summary=summary,
            description=description,
            issuetype={'name': 'Epic'}
        )

        print(f"   Created: {issue.key}")
        return issue.key

    def create_story(self, summary: str, description: str, epic_key: str = None,
                     story_points: int = None) -> str:
        """Create user story"""

        print(f"📖 Creating story: {summary}")

        fields = {
            'project': self.project_key,
            'summary': summary,
            'description': description,
            'issuetype': {'name': 'Story'}
        }

        if epic_key:
            fields['parent'] = {'key': epic_key}

        if story_points:
            fields['customfield_10016'] = story_points  # Story points field

        issue = self.jira.create_issue(fields=fields)

        print(f"   Created: {issue.key}")
        return issue.key

    def create_subtask(self, parent_key: str, summary: str, assignee: str = None) -> str:
        """Create subtask"""

        print(f"   📌 Creating subtask: {summary}")

        fields = {
            'project': self.project_key,
            'summary': summary,
            'issuetype': {'name': 'Sub-task'},
            'parent': {'key': parent_key}
        }

        if assignee:
            fields['assignee'] = {'name': assignee}

        issue = self.jira.create_issue(fields=fields)

        print(f"      Created: {issue.key}")
        return issue.key

    def transition_issue(self, issue_key: str, transition_name: str):
        """Transition issue to new status"""

        print(f"🔄 Transitioning {issue_key} to {transition_name}")

        # Get available transitions
        transitions = self.jira.transitions(issue_key)

        # Find matching transition
        for t in transitions:
            if t['name'].lower() == transition_name.lower():
                self.jira.transition_issue(issue_key, t['id'])
                print(f"   ✅ Transitioned to {transition_name}")
                return

        print(f"   ❌ Transition '{transition_name}' not found")

    def add_comment(self, issue_key: str, comment: str):
        """Add comment to issue"""

        self.jira.add_comment(issue_key, comment)
        print(f"💬 Added comment to {issue_key}")

    def link_issues(self, inward_issue: str, outward_issue: str, link_type: str = "Blocks"):
        """Create link between issues"""

        print(f"🔗 Linking {inward_issue} {link_type} {outward_issue}")

        self.jira.create_issue_link(
            type=link_type,
            inwardIssue=inward_issue,
            outwardIssue=outward_issue
        )

    def create_sprint_workflow(self) -> Dict:
        """Create complete sprint workflow"""

        print("\n" + "=" * 60)
        print("🏃 Creating Sprint Workflow")
        print("=" * 60)

        # Create epic
        epic_key = self.create_epic(
            summary="User Authentication System",
            description="Implement complete user authentication with OAuth2"
        )

        # Create stories
        stories = []

        story1 = self.create_story(
            summary="Login functionality",
            description="Users should be able to login with email/password",
            epic_key=epic_key,
            story_points=5
        )
        stories.append(story1)

        # Add subtasks to story 1
        self.create_subtask(story1, "Design login UI")
        self.create_subtask(story1, "Implement backend API")
        self.create_subtask(story1, "Add form validation")
        self.create_subtask(story1, "Write unit tests")

        story2 = self.create_story(
            summary="OAuth2 integration",
            description="Integrate Google and GitHub OAuth2",
            epic_key=epic_key,
            story_points=8
        )
        stories.append(story2)

        story3 = self.create_story(
            summary="Password reset flow",
            description="Allow users to reset forgotten passwords",
            epic_key=epic_key,
            story_points=3
        )
        stories.append(story3)

        # Link dependencies
        self.link_issues(story1, story2, "Blocks")

        # Add comments
        self.add_comment(story1, "Starting development on this story")

        # Transition stories
        self.transition_issue(story1, "In Progress")

        print("\n✅ Sprint workflow created!")

        return {
            'epic': epic_key,
            'stories': stories
        }

    def generate_report(self, project_key: str = None) -> Dict:
        """Generate project report"""

        if not project_key:
            project_key = self.project_key

        print(f"\n📊 Generating report for {project_key}")
        print("=" * 60)

        # Get all issues
        issues = self.jira.search_issues(f'project={project_key}', maxResults=100)

        # Count by type
        by_type = {}
        by_status = {}
        total_story_points = 0

        for issue in issues:
            # By type
            issue_type = issue.fields.issuetype.name
            by_type[issue_type] = by_type.get(issue_type, 0) + 1

            # By status
            status = issue.fields.status.name
            by_status[status] = by_status.get(status, 0) + 1

            # Story points
            if hasattr(issue.fields, 'customfield_10016') and issue.fields.customfield_10016:
                total_story_points += issue.fields.customfield_10016

        print(f"\nTotal Issues: {len(issues)}")

        print(f"\nBy Type:")
        for itype, count in by_type.items():
            print(f"  {itype}: {count}")

        print(f"\nBy Status:")
        for status, count in by_status.items():
            print(f"  {status}: {count}")

        print(f"\nTotal Story Points: {total_story_points}")

        return {
            'total_issues': len(issues),
            'by_type': by_type,
            'by_status': by_status,
            'story_points': total_story_points
        }

    def automate_daily_tasks(self):
        """Automate daily Jira tasks"""

        print("\n🤖 Running Daily Automation")
        print("=" * 60)

        # 1. Find stale issues (no updates in 7 days)
        jql = f'project={self.project_key} AND updated < -7d AND status != Done'
        stale_issues = self.jira.search_issues(jql)

        print(f"\n⚠️  Found {len(stale_issues)} stale issues:")
        for issue in stale_issues:
            print(f"   {issue.key}: {issue.fields.summary}")
            self.add_comment(
                issue.key,
                "This issue hasn't been updated in 7 days. Please provide an update."
            )

        # 2. Auto-close completed subtasks' parents
        jql = f'project={self.project_key} AND issuetype=Story AND status="In Progress"'
        stories = self.jira.search_issues(jql)

        for story in stories:
            subtasks = story.fields.subtasks
            if subtasks:
                all_done = all(
                    self.jira.issue(st.key).fields.status.name == 'Done'
                    for st in subtasks
                )

                if all_done:
                    print(f"\n✅ All subtasks done for {story.key}, transitioning to Done")
                    self.transition_issue(story.key, "Done")

        # 3. Send summary
        report = self.generate_report()

        print("\n✅ Daily automation complete!")

        return report

def main():
    """Run Jira automation demo"""

    print("📋 Jira Workflow Automation")
    print("=" * 60)

    # Initialize
    jira = JiraAutomation()

    # Create project
    jira.create_project("DEMO", "Demo Project", "admin")

    # Create sprint workflow
    workflow = jira.create_sprint_workflow()

    # Generate report
    jira.generate_report()

    # Run daily automation
    jira.automate_daily_tasks()

    print("\n" + "=" * 60)
    print("✨ Automation complete!")
    print("=" * 60)

if __name__ == "__main__":
    # Install: pip install jira
    # Note: Update JIRA_SERVER, JIRA_USER, JIRA_TOKEN before running
    main()

"""
AutoGen - Two-Agent Code Review Pipeline
Demonstrates: Automated code review with coder + reviewer + executor pattern
"""

import os
import autogen
from autogen import AssistantAgent, UserProxyAgent
from autogen.coding import LocalCommandLineCodeExecutor
from pathlib import Path

llm_config = {
    "config_list": [
        {
            "model": os.getenv("OLLAMA_MODEL", "llama3"),
            "base_url": "http://ollama:11434/v1",
            "api_key": "ollama",
        }
    ],
    "temperature": 0.1,
}

executor = LocalCommandLineCodeExecutor(
    timeout=20,
    work_dir=Path("/tmp/autogen_code_review"),
)

coder = AssistantAgent(
    name="Coder",
    llm_config=llm_config,
    system_message=(
        "You are an expert Python developer. Write clean, secure, production-ready code. "
        "Include type hints, error handling, and docstrings. "
        "When code is ready, wrap it in ```python ... ``` blocks."
    ),
)

reviewer = AssistantAgent(
    name="CodeReviewer",
    llm_config=llm_config,
    system_message=(
        "You are a senior code reviewer. Review code for: "
        "1) Security (OWASP Top 10) "
        "2) Performance "
        "3) Code quality (PEP 8, type safety) "
        "4) Error handling "
        "Provide specific line-by-line feedback. "
        "If code passes all checks, respond with 'APPROVED: TERMINATE'."
    ),
)

executor_proxy = UserProxyAgent(
    name="Executor",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=3,
    is_termination_msg=lambda x: "TERMINATE" in x.get("content", ""),
    code_execution_config={"executor": executor},
)


def review_code_task(task_description: str):
    """Run a code generation + review cycle."""
    print(f"\nTask: {task_description}\n{'='*50}")

    # Coder writes code, reviewer reviews, executor runs tests
    result = executor_proxy.initiate_chats([
        {
            "recipient": coder,
            "message": f"Write Python code for: {task_description}",
            "max_turns": 3,
            "summary_method": "last_msg",
        },
        {
            "recipient": reviewer,
            "message": "Review the code above for security, performance, and quality.",
            "max_turns": 3,
            "summary_method": "last_msg",
        },
    ])
    return result


if __name__ == "__main__":
    review_code_task(
        "A FastAPI endpoint that accepts a service name, checks its Docker container "
        "health via subprocess, and returns a JSON health report. "
        "Must be secure (no shell injection), handle errors, and have proper typing."
    )

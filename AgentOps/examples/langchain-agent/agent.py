"""
LangChain ReAct Agent with Tools
Demonstrates: Agent reasoning, tool usage, memory, callbacks
"""

from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools import Tool
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.callbacks import StdOutCallbackHandler
import requests
from datetime import datetime
import json

# Ollama endpoint
OLLAMA_URL = "http://localhost:11434"

# Custom tools
def get_current_weather(location: str) -> str:
    """Get current weather for a location"""
    # Simulated weather API
    weather_data = {
        "New York": "Sunny, 72°F",
        "London": "Cloudy, 15°C",
        "Tokyo": "Rainy, 20°C",
    }
    return weather_data.get(location, f"Weather data not available for {location}")

def search_web(query: str) -> str:
    """Search the web for information"""
    # Simulated search (in production, use real API)
    return f"Search results for '{query}': [Simulated results would appear here]"

def calculate(expression: str) -> str:
    """Perform mathematical calculations"""
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error in calculation: {str(e)}"

def get_current_time() -> str:
    """Get current date and time"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def create_agent():
    """Create LangChain agent with tools"""

    # Initialize LLM (Ollama)
    llm = Ollama(
        base_url=OLLAMA_URL,
        model="llama2",
        temperature=0.7
    )

    # Define tools
    tools = [
        Tool(
            name="Weather",
            func=get_current_weather,
            description="Get current weather for a location. Input should be a city name."
        ),
        Tool(
            name="Search",
            func=search_web,
            description="Search the web for information. Input should be a search query."
        ),
        Tool(
            name="Calculator",
            func=calculate,
            description="Perform mathematical calculations. Input should be a mathematical expression."
        ),
        Tool(
            name="Time",
            func=get_current_time,
            description="Get current date and time. No input needed."
        ),
    ]

    # Create prompt template
    prompt = PromptTemplate.from_template("""
    Answer the following questions as best you can. You have access to the following tools:

    {tools}

    Use the following format:

    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer
    Final Answer: the final answer to the original input question

    Begin!

    Question: {input}
    Thought: {agent_scratchpad}
    """)

    # Create agent
    agent = create_react_agent(llm, tools, prompt)

    # Create agent executor
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        max_iterations=5,
        handle_parsing_errors=True
    )

    return agent_executor

def run_agent_task(agent: AgentExecutor, task: str):
    """Run a single agent task"""
    print(f"\n{'=' * 60}")
    print(f"Task: {task}")
    print('=' * 60)

    try:
        result = agent.invoke({"input": task})
        print(f"\n✅ Final Answer: {result['output']}")
        return result['output']
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        return None

def main():
    """Demo agent capabilities"""

    print("🤖 LangChain ReAct Agent Demo")
    print("=" * 60)

    # Create agent
    print("\n🔧 Initializing agent...")
    agent = create_agent()
    print("✅ Agent ready with tools: Weather, Search, Calculator, Time")

    # Example tasks
    tasks = [
        # Simple tool usage
        "What's the weather like in New York?",

        # Calculation
        "What is 15% of 250?",

        # Multiple steps
        "What time is it and what's the weather in London?",

        # Reasoning required
        "If I have $100 and want to buy items that cost $15, $23, and $42, how much money will I have left?",

        # Search required
        "Search for information about machine learning",
    ]

    results = []

    for task in tasks:
        result = run_agent_task(agent, task)
        results.append({
            'task': task,
            'result': result
        })

    # Summary
    print("\n" + "=" * 60)
    print("📊 Summary")
    print("=" * 60)

    successful = sum(1 for r in results if r['result'] is not None)
    print(f"\nCompleted: {successful}/{len(tasks)} tasks")

    print("\n" + "=" * 60)
    print("✨ Demo complete!")
    print("=" * 60)

def interactive_mode():
    """Interactive agent session"""

    print("🤖 Interactive Agent Mode")
    print("=" * 60)
    print("Available tools: Weather, Search, Calculator, Time")
    print("Type 'quit' to exit\n")

    agent = create_agent()

    while True:
        task = input("\nYou: ").strip()

        if task.lower() in ['quit', 'exit', 'q']:
            print("Goodbye! 👋")
            break

        if not task:
            continue

        run_agent_task(agent, task)

if __name__ == "__main__":
    # Install: pip install langchain langchain-community

    import sys

    if len(sys.argv) > 1 and sys.argv[1] == 'interactive':
        interactive_mode()
    else:
        main()

import os
from dotenv import load_dotenv
from crewai import Agent,Task,Crew,LLM
from crewai.tools import BaseTool
from google import genai

load_dotenv()

# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

#Gemini Wrapper
gemini_llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)

class SearchTool(BaseTool):
    name: str = "search_tool"
    description: str = "Search for information about a given topic"

    def _run(self, query: str) -> str:
        print(f"\n[TOOL USED] Searching for: {query}\n")

        return f"""
        Search Results for {query}:

        - {query} is an important concept in modern technology.
        - It involves key principles and real-world applications.
        - Understanding it helps in building scalable systems.
        """

# -------------------------------
# 🤖 AGENTS
# -------------------------------

researcher = Agent(
    role="Researcher",
    goal="Find accurate information using tools",
    backstory="You are an expert researcher who uses tools to gather information",
    tools=[SearchTool()],  # 🔥 LEVEL 3
    llm=gemini_llm,
    verbose=True
)

writer = Agent(
    role="Writer",
    goal="Explain things clearly and simply",
    backstory="You are great at simplifying complex topics",
    llm=gemini_llm,
    verbose=True
)

# -------------------------------
# 📋 TASKS
# -------------------------------

topic = input("Enter topic: ")

research_task = Task(
    description=f"""
    Research about {topic}.

    IMPORTANT:
    - You MUST use the search_tool to gather information
    - Then summarize key points clearly
    """,
    agent=researcher,
    expected_output="Bullet points"
)

write_task = Task(
    description=f"""
    Explain {topic} in simple terms using the research provided.
    """,
    agent=writer,
    expected_output="Simple explanation"
)

# -------------------------------
# 🚀 CREW
# -------------------------------

crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    verbose=True
)
result = crew.kickoff()
print("\nFinal Output:\n", result)
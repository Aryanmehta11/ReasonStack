from crewai import Agent, LLM
from tools import SearchTool
import os

gemini_llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)

researcher = Agent(
    role="Researcher",
    goal="Find accurate information",
    backstory="Expert researcher",
    tools=[SearchTool()],
    llm=gemini_llm,
    verbose=True
)

critic = Agent(
    role="Critic",
    goal="Ensure quality research",
    backstory="Strict reviewer",
    llm=gemini_llm,
    verbose=True
)

writer = Agent(
    role="Writer",
    goal="Simplify topics",
    backstory="Great explainer",
    llm=gemini_llm,
    verbose=True
)

reviewer = Agent(
    role="Reviewer",
    goal="Polish final output",
    backstory="Final quality check",
    llm=gemini_llm,
    verbose=True
)
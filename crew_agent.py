import os
from dotenv import load_dotenv
from crewai import Agent,Task,Crew,LLM
from crewai.tools import BaseTool
from google import genai
from tavily import TavilyClient
from langsmith import traceable

load_dotenv()

os.environ["LANGSMITH_TRACING"]="true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = "Research Agent"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"


# client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

#Gemini Wrapper
gemini_llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)

class SearchTool(BaseTool):
    name: str = "search_tool"
    description: str = "Search the web for real, accurate information about a topic"

    def _run(self, query: str) -> str:
        print(f"\n[TOOL USED] Searching Tavily for: {query}\n")
        
        try:
            client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
            
            response = client.search(
                query=query,
                search_depth="advanced",  # deeper search
                max_results=5             # get 5 results
            )
            
            # Extract and format results
            results = []
            for r in response.get("results", []):
                results.append(f"""
                📌 Title: {r['title']}
                🔗 Source: {r['url']}
                📝 Summary: {r['content']}
                """)
            
            return "\n".join(results) if results else "No results found."
        
        except Exception as e:
            return f"Search failed: {str(e)}"





# -------------------------------
# 🤖 AGENTS
# -------------------------------

researcher = Agent(
    role="Researcher",
    goal="Find accurate information using tools",
    backstory="You are an expert researcher who uses tools to gather information",
    tools=[SearchTool()],
    llm=gemini_llm,
    verbose=True
)

critic=Agent(
     role="Critic",
    goal="Review research quality and demand improvements if needed",
    backstory="""You are a strict quality reviewer. You check if 
    research is detailed enough. If not, you clearly state what 
    is missing and request improvements.""",
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


reviewer = Agent(
    role="Reviewer",
    goal="Ensure the final writing is clear and beginner friendly",
    backstory="""You review written content and improve it if 
    it is too complex, incomplete, or unclear. You always 
    deliver a polished final output.""",
    llm=gemini_llm,
    verbose=True
)

# -------------------------------
# 📋 TASKS
# -------------------------------

topic = input("Enter topic to research: ")

research_task = Task(
    description=f"""
    Research the topic: {topic}

    STRICT RULES:
    - You MUST use search_tool at least once
    - Collect minimum 5 key points
    - Include: definition, use cases, benefits, challenges
    - Be specific, not vague
    """,
    agent=researcher,
    expected_output="Detailed bullet points covering definition, \
    use cases, benefits, and challenges"
)

critic_task = Task(
    description=f"""
    Review the research about {topic}.

    CHECK FOR:
    - Is there a clear definition?
    - Are there real use cases?
    - Are benefits AND challenges covered?
    - Is it detailed enough (minimum 5 points)?

    If research is INCOMPLETE:
    - Clearly list what is missing
    - Rewrite and improve the research yourself

    If research is COMPLETE:
    - Approve it and pass it along
    """,
    agent=critic,
    expected_output="Either approved research OR improved \
    research with missing points filled in",
    context=[research_task]
)

write_task = Task(
    description=f"""
    Using the reviewed research, explain {topic} simply.

    REQUIREMENTS:
    - Write for a complete beginner
    - Use simple language, no jargon
    - Include real examples
    - Minimum 3 paragraphs
    """,
    agent=writer,
    expected_output="A beginner friendly explanation with examples",
    context=[critic_task]
)

review_task = Task(
    description=f"""
    Review the written explanation about {topic}.

    CHECK:
    - Is it simple enough for beginners?
    - Are examples clear and relevant?
    - Is anything confusing or missing?

    If writing needs improvement:
    - Fix it and produce a better version

    If writing is good:
    - Polish it and deliver the final version
    """,
    agent=reviewer,
    expected_output="Final polished explanation ready for beginners",
    context=[write_task]
)


# -------------------------------
# 🚀 CREW
# -------------------------------

@traceable(name="Research Agent Pipeline") 
def run_pipeline():
    crew = Crew(
        agents=[researcher, critic,writer,reviewer],
        tasks=[research_task, critic_task, write_task,review_task],
        verbose=True
    )
    result=crew.kickoff()
    return result
result = run_pipeline()
print("\nFinal Output:\n", result)
print("="*50)
print(result)

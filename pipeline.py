from crewai import Crew, Task
from agents import researcher, critic, writer, reviewer
from langsmith import traceable

@traceable(name="Research Agent Pipeline")
def run_pipeline(topic: str):

    research_task = Task(
        description=f"""
        Research the topic: {topic}
        STRICT RULES:
        - Use search_tool at least once
        - Include definition, use cases, benefits, challenges
        """,
        agent=researcher,
        expected_output="Detailed research with at least 5 key points including definition, use cases, benefits, and challenges"
    )

    critic_task = Task(
        description=f"Review research about {topic}",
        agent=critic,
        context=[research_task],
        expected_output="Improved or approved research with missing gaps filled"
    )

    write_task = Task(
        description=f"Explain {topic} simply",
        agent=writer,
        context=[critic_task],
        expected_output="Beginner-friendly explanation with examples"
    )

    review_task = Task(
        description=f"Polish explanation about {topic}",
        agent=reviewer,
        context=[write_task],
        expected_output="Final polished explanation"
    )

    crew = Crew(
        agents=[researcher, critic, writer, reviewer],
        tasks=[research_task, critic_task, write_task, review_task],
        verbose=True,
        memory=False   # 🔥 important
    )

    return crew.kickoff(inputs={"topic": topic})
from crewai.tools import BaseTool
from tavily import TavilyClient
import os, time

class SearchTool(BaseTool):
    name: str = "search_tool"
    description: str = "Search web for accurate info"

    def _run(self, query: str) -> str:
        for attempt in range(3):
            try:
                client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

                response = client.search(
                    query=query,
                    search_depth="advanced",
                    max_results=5
                )

                results = []
                for r in response.get("results", []):
                    results.append(f"""
                    📌 {r['title']}
                    🔗 {r['url']}
                    📝 {r['content']}
                    """)

                return "\n".join(results)

            except Exception as e:
                if attempt < 2:
                    time.sleep(1)
                else:
                    return f"Search failed: {str(e)}"
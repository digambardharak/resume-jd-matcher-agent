import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

tavily_api_key = os.getenv("TAVILY_API_KEY")
tavily_client = TavilyClient(api_key=tavily_api_key)

def find_resources_for_skill(skill, max_results=3):
    """Search for learning resources for a given missing skill."""
    query = f"best free course or tutorial to learn {skill}"

    try:
        response = tavily_client.search(query=query, max_results=max_results)
        results = response.get("results", [])
        resources = [{"title": r["title"], "url": r["url"]} for r in results]
        return resources
    except Exception as e:
        print(f"Error searching for {skill}: {e}")
        return []


def get_resources_for_missing_skills(missing_skills, max_skills=3):
    """For the top N missing skills, find learning resources for each."""
    resource_map = {}
    for skill in missing_skills[:max_skills]:
        resource_map[skill] = find_resources_for_skill(skill)
    return resource_map


if __name__ == "__main__":
    # Quick test
    test_skills = ["LLMs", "Agentic AI"]
    results = get_resources_for_missing_skills(test_skills)
    for skill, resources in results.items():
        print(f"\n{skill}:")
        for r in resources:
            print(f"  - {r['title']} ({r['url']})")
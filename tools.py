from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os
from dotenv import load_dotenv
load_dotenv()
from rich import print

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query : str) -> str:
    """Searches the Web for recent and Reliable Information on a Topic. Returns Titles, URLs and Snippets."""
    results = tavily.search(query=query, max_results=5)
    return results 

print(web_search.invoke("what are the recent news on war ?"))
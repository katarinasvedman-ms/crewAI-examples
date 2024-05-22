from crewai import Agent
from textwrap import dedent
from langchain_openai import AzureChatOpenAI
from tools.calculator_tools import CalculatorTools
from tools.search_tools import SearchTools
from tools.browser_tools import BrowserTools


default_llm = AzureChatOpenAI(
    openai_api_version="2023-07-01-preview",
    azure_deployment="gpt-4-32k",
    azure_endpoint="",
    api_key=""
)

# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class TripAgents():

    def city_selection_agent(self):
        return Agent(
            role='City Selection Expert',
            goal='Select the best city from {cities} based on weather, season, and prices',
            backstory=
            'An expert in analyzing travel data to pick ideal destinations',
            tools=[
                SearchTools.search_internet,
                #BrowserTools.scrape_and_summarize_website,
            ],
            verbose=True,
            llm=default_llm
        )

    def local_expert(self):
        return Agent(
            role='Local Expert at this city',
            goal='Provide the BEST insights about the selected city',
            backstory="""A knowledgeable local guide with extensive information
            about the city, it's attractions and customs""",
            tools=[
                SearchTools.search_internet,
                #BrowserTools.scrape_and_summarize_website,
            ],
            verbose=True,
            llm=default_llm
        )
    
    def travel_concierge(self):
        return Agent(
            role='Amazing Travel Concierge',
            goal="""Create the most amazing travel itineraries with budget and 
            packing suggestions for the city""",
            backstory="""Specialist in travel planning and logistics with 
            decades of experience""",
            tools=[
                SearchTools.search_internet,
                #BrowserTools.scrape_and_summarize_website,
                CalculatorTools.calculate,
            ],
            verbose=True,
            llm=default_llm
        )

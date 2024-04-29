from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI

from tools.search_tools import SearchTools

""""    
Creating Agents Cheat Sheet:
- Think like a boss.  Work backwards from the goal and think which employee you need to hire to get the job done.
- Define the captain of the crew who orient the other agents toward the goal.
- define which experts the captain needs to communicate with and delegate tasks to.
    Build a top down structure of the crew.

Goal: Create a Newsletter that summarizes any laws/legislation that are coming through the US Congress.
        This should be updated regularly as new laws/bills are created and in line for review.
        The newsletter should have the law/article/legislation #, high level summary, political party alignment/driver,
        Impact to the general public, statutes.

Captain/Manager/Boss: 
- Role: Expert Policy Advisor

Employees/Experts to hire:
- Role: Web Scraper Agent
- Role: Data Processor Agent
- Role: Legislative Analyst Agent

Notes: 
Agents should be results driven and have clear goal in mind
role is their job title
goals should be actionable
Backstory should be their resume
"""

# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class PolicyPulseAgents:
    def __init__(self):
        #self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        #self.Ollama = Ollama(model="openhermes")

    def expert_policy_advisor(self):
        return Agent(
            role="Expert Policy Advisor",
            backstory=dedent(f"""
                             Expert in summarizes laws/legislation. I have decades of experience analyzing
                             new laws/legislation & helping the general public understand them and how it may impact their lives.
                             """),
            goal=dedent(f"""
                        Create a newsletter that summarizes laws & legislation that are making their way through the US Congress.
                        This should include the law/article/legislation #, a high level overview of the item,
                        political party alignment, and the law/item's impact the the general public.
                        """),
            # tools=[tool_1, tool_2],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4,
        )

    def web_scraper_expert(self):
        return Agent(
            role="Web Scraper/Searcher Expert",
            backstory=dedent(f"""
                             Expert at searching the internet and finding the best resources for laws/legislation
                             that are actively being brought through Congress.
                             """),
            goal=dedent(f"""
                        Search online to find all laws/legislation that are coming through the US Congress.
                        This should not include laws/legislation that are already in place.  Find the best resource online that
                        has a full database of the laws/legislation.
                        """),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4,
        )
    
    def expert_legislative_analyst(self):
        return Agent(
            role="Expert Legislative Analyst",
            backstory=dedent(f"""
                             Expert and Summarizing & Analyzing laws and legislation that are being brought through the US Congress.
                             Decades of experience on laws/legislation & experience with summarizing them for the general population.
                             """),
            goal=dedent(f"""
                        Provide detailed breakdown & analysis of the laws/legislation that you receive from the Web Scraper Expert.
                        You should take the given law/legislation and generate the following: law/legislation id or number, high level summary
                        of the law/legislation, law/legislation's political favorment/alignment, and the law/legislation impact to the general public.
                        """),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT4,
        )

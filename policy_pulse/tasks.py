from crewai import Task # type: ignore
from textwrap import dedent

"""
Creating tasks cheat sheet:
- begin with the end in mind.  Identity the specific outcome your tasks are aiming to achieve
- break down the outcome into actionable tasks, assigning each task to appropriate agent.
- ensure tasks are descriptive, providing clear instructions and expected deliverables

Goal:
- Develop a report/newsletter, including law/legislation name & ID/#, high level overview, political alignment, and impact of the law on the general public

Key Steps for Task Creation:
- Identify desired outcome: Create a detailed list of all new/existing laws/legislation that are going through congress.
    - this should include the law/legislation number and title, a high level summary, alignment to political party, and the impact the bill has on the general public

Task Breakdown:
- Newsletter/Report Creation: Develop a report that outlines with key information, the laws/legislation coming through congress
- Web searcher: Search the internet for the best sites/links that have all of the new/existing laws/legislation going through Congress
- Legislative Analyst: Review the data that gets passed from the web searcher. Analyze the laws/legislation, and break 
                        them down with the follwing details: law/legislation id & title, high level summary of bill,
                        political affiliation, impact on the general public
"""

# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class PolicyPulseTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def create_detailed_report(self, agent):
        return Task(
            description=dedent(
                f"""
            **Task**: Develop a detailed Report on laws/legislation that are actively going through the US Congress.
            **Description**: Expand on the inputs from the legislative analyst and generate a detailed report that outlines
            new laws/legislation that are coming through the US Congress.  This must include the title and ID of the bill, a
            high level summary/overview of the bill, which political party the bill aligns with, and what the impact of the bill has
            on the general public.

            **Note**: {self.__tip_section()}
            """

        ),   
        agent=agent,
    )

    def web_search(self, agent):
        return Task(
            description=dedent(
                f"""
                **Task**: Search the internet to find all of the new laws/bills/legislation that are actively going
                through the US Congress.
                **Description**: Analyze existing websites to determine which site has the most accurate and up to date 
                information on bills/laws going through Congress.  After careful analysis, decide on which website should
                be our source of truth for the most accuraute list of laws/bills.  Your final answer should be a specific
                website which can be passed along to the analyst to then pull the necessary information on each bill/law
                which will be aggregated into a full report.
                
                **Note**: {self.__tip_section()}=
                """
        ),
            agent=agent,
    )

    def legislative_analysis(self, agent):
        return Task(
            description=dedent(
                f"""
                **Task**: Do In-Depth analysis on the laws/bills going through Congress that are listed in the website provided to you.
                **Description**: Choose the most recent law/bill that is listed out on the website to start.  You should do a thorough analysis
                of the bill/law based on your legislative expertise.  Pull out the ID/# of the bill, the title/name of the bill, generate a high 
                level summary of the bill, determine which political party the bill aligns with, and provide an impact analysis on how the bill/law
                impacts the general public in a positive/negative way.

                **Note**: {self.__tip_section()}
                """
        ),
        agent=agent,
    )

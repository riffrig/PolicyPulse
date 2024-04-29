from crewai import Crew
from textwrap import dedent
from agents import PolicyPulseAgents
from tasks import PolicyPulseTasks

from dotenv import load_dotenv
load_dotenv()

# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py


class PolicyPulseCrew:
    def __init__(self):
        self.my_attribute = "Hello, world!"

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = PolicyPulseAgents()
        tasks = PolicyPulseTasks()

        # Define your custom agents and tasks here
        expert_policy_advisor = agents.expert_policy_advisor()
        web_scraper_expert = agents.web_scraper_expert()
        expert_legislative_analyst = agents.expert_legislative_analyst()

        # Custom tasks include agent name and variables as input
        create_detailed_report = tasks.create_detailed_report(
            expert_policy_advisor,
        )

        web_search = tasks.web_search(
            web_scraper_expert,
        )

        legislative_analysis = tasks.legislative_analysis(
            expert_legislative_analyst,
        )

        # Define your custom crew here
        crew = Crew(
            agents=[expert_policy_advisor, web_scraper_expert, expert_legislative_analyst],
            tasks=[create_detailed_report, web_search, legislative_analysis],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to the Policy Pulse Crew")
    print("-------------------------------")

    policy_pulse_crew = PolicyPulseCrew()
    result = policy_pulse_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)

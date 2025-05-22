from crewai import Crew,Process
from tasks import research_task, write_task, proof_read_task
from agents import researcher, writer, proof_reader


crew = Crew(
    agents= [researcher, writer, proof_reader],
    tasks=[research_task, write_task, proof_read_task],
    process=Process.sequential
)

topic="Artificial Intelligence in Finance"
result=crew.kickoff(inputs={"topic":topic})
print(result)
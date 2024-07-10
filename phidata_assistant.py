from phi.assistant import Assistant, AssistantMemory
from phi.llm.anthropic import Claude
import os
from dotenv import load_dotenv

load_dotenv() 

class AssistantInterface:
    def __init__(self, description, name):
        self.assistant = Assistant(
            description=description,
            llm=Claude(model="claude-3-5-sonnet-20240620", api_key=os.getenv("ANTHROPIC_API_KEY")),
            name=name,
            memory=AssistantMemory(),
            tools=[],
            debug_mode=True
        )

    def get_response(self, message, stream=True):
        return self.assistant.run(message, stream=stream)

# Initialize the AssistantInterface
assistant_interface = AssistantInterface(
    description="You help people with their health and fitness goals.",
    name="Health and Fitness Assistant"
)
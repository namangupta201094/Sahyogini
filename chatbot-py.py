import logging
from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter

logger = logging.getLogger(__name__)

class Chatbot:
    def __init__(self, knowledge_graph, llm_interface, data_manager):
        self.knowledge_graph = knowledge_graph
        self.llm_interface = llm_interface
        self.data_manager = data_manager
        self.agent = Agent.load("path/to/your/rasa/model")
        self.interpreter = RasaNLUInterpreter("path/to/your/nlu/model")

    async def handle_message(self, message, user_id):
        # Get user profile
        user_profile = self.data_manager.get_user_profile(user_id)

        # Use Rasa to understand the intent and entities
        interpretation = await self.interpreter.parse(message)
        intent = interpretation['intent']['name']
        entities = interpretation['entities']

        # Get relevant information from knowledge graph
        scheme_info = self.knowledge_graph.get_scheme(intent)

        # Generate response using LLM
        llm_response = self.llm_interface.generate_response(message, scheme_info)

        # Personalize the response
        personalized_response = self.llm_interface.personalize_response(llm_response, user_profile)

        return personalized_response

    async def train(self, training_data):
        # Train the Rasa model
        self.agent = await Agent.train(
            training_data,
            output_path="path/to/save/model",
            fixed_model_name="sahyogini_model"
        )

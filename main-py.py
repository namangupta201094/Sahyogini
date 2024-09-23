import logging
from scraper import Scraper
from knowledge_graph import KnowledgeGraph
from llm_interface import LLMInterface
from chatbot import Chatbot
from telegram_bot import TelegramBot
from data_manager import DataManager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    logger.info("Starting Sahyogini application")
    
    # Initialize components
    scraper = Scraper()
    knowledge_graph = KnowledgeGraph()
    llm_interface = LLMInterface()
    data_manager = DataManager()
    chatbot = Chatbot(knowledge_graph, llm_interface, data_manager)
    telegram_bot = TelegramBot(chatbot)

    # Start the Telegram bot
    telegram_bot.start()

if __name__ == "__main__":
    main()

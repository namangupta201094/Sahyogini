import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logger = logging.getLogger(__name__)

class TelegramBot:
    def __init__(self, chatbot):
        self.token = "your-telegram-bot-token"  # Replace with your actual Telegram bot token
        self.chatbot = chatbot
        self.updater = Updater(token=self.token, use_context=True)
        self.dispatcher = self.updater.dispatcher

        # Add handlers
        self.dispatcher.add_handler(CommandHandler("start", self.start))
        self.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, self.handle_message))

    def start(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to Sahyogini! How can I assist you today?")

    def handle_message(self, update, context):
        user_id = update.effective_user.id
        message = update.message.text
        response = self.chatbot.handle_message(message, user_id)
        context.bot.send_message(chat_id=update.effective_chat.id, text=response)

    def start(self):
        logger.info("Starting Telegram bot")
        self.updater.start_polling()
        self.updater.idle()

from telegram.ext import Updater
from telegram.ext import CommandHandler
import os
import db_tools
import configparser


class ComplimentBotListener:

    def __init__(self, token, welcome_message="Hey there!", goodbye_message="Bye!"):

        # Initialising updater and dispatcher
        self.updater = Updater(token=token)
        self.dispatcher = self.updater.dispatcher

        # Welcome and goodbye messages
        self.welcome_message = welcome_message
        self.goodbye_message = goodbye_message

        # Connecting to database
        path = os.path.dirname(os.path.realpath(__file__))
        db_dirname = os.path.join(path, 'db')
        self.db_tools = db_tools.DBTools(db_dirname)

        # Adding a handler for "/start"
        start_handler = CommandHandler('start', self.start)
        self.dispatcher.add_handler(start_handler)

        # Adding a handler for "/stop"
        stop_handler = CommandHandler('stop', self.stop)
        self.dispatcher.add_handler(stop_handler)

        # Start listening
        self.updater.start_polling()

    def start(self, bot, update):
        chat_id = update.message.chat_id
        # record chat in database
        self.db_tools.save_chat(chat_id)
        bot.send_message(chat_id=chat_id, text=self.welcome_message)

    def stop(self, bot, update):
        chat_id = update.message.chat_id
        self.db_tools.delete_chat(chat_id)
        bot.send_message(chat_id=chat_id, text=self.goodbye_message)


def main():
    path = os.path.dirname(os.path.realpath(__file__))
    config = configparser.RawConfigParser()
    config.read(os.path.join(path, 'config', 'bot.cfg'))
    bot = ComplimentBotListener(config.get('api', 'token'))


if __name__ == '__main__':
    main()

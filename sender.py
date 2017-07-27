import telegram.bot
import configparser
import os
import db_tools
import message_constructor


def main():
    # Loading config file
    path = os.path.dirname(os.path.realpath(__file__))
    config = configparser.RawConfigParser()
    config.read(os.path.join(path, 'config', 'bot.cfg'))

    # Initialising bot
    bot = telegram.bot.Bot(config.get('api', 'token'))

    # Loading all chat ids from the database
    db_dirname = os.path.join(path, 'db')
    db = db_tools.DBTools(db_dirname)
    chat_ids = db.get_all_chats()

    # Building and sending messages to every chat
    for chat_id in chat_ids:
        bot.send_message(chat_id=chat_id, text=message_constructor.build_message())

if __name__ == '__main__':
    main()

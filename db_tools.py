from tinydb import TinyDB, Query
import os


class DBTools:

    def __init__(self, path):
        path = os.path.join(path, 'db.json')
        db = TinyDB(path)
        self.db = db
        self.chats_table = db.table('Chats')

    def save_chat(self, chat_id):
        chat = Query()
        # do nothing if already in database
        if self.chats_table.search(chat.chat_id == chat_id):
            return
        self.chats_table.insert({'chat_id': chat_id})

    def get_all_chats(self):
        return [item['chat_id'] for item in self.chats_table.all()]

    def delete_chat(self, chat_id):
        chat = Query()
        self.chats_table.remove(chat.chat_id == chat_id)

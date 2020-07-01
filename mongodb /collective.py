from pymongo import MongoClient
from config import monogoDB, db, collec
import datetime


class Collectives:
    def __init__(self, col):
        client = MongoClient(monogoDB)
        self.database = client[db]
        self.col = col

    def check_collections(self):
        for x in self.database.list_collection_names():
            if x == self.col:
                return False
            else:
                return self.database[self.col]

    def add_message(self, username, message):
        if len(message) == 0:
            return False, 'No Message'
        temp_status = self.check_collections()
        if not temp_status:
            return temp_status, 'Not Allowed'
        else:
            col_ledger = temp_status
        query = {'collective_name': self.col, 'username': username, 'message': message,
                 'time': datetime.datetime.now()}
        col_ledger.insert_one(query)
        return True, 'Message Added'

# print(Collectives('user').check_collections())
print(Collectives('users').add_message('test','test'))
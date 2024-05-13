import asyncio
from threading import RLock
from pymongo import MongoClient
from config import MURALI_DB
from CUTEXMUSIC.utils.msg_types import Types

INSERTION_LOCK = RLock()

class Floods:
    """Class to store flood limit and action of a chat"""
    db_name = "flood"

    def __init__(self):
        self.client = MongoClient(MURALI_DB)
        self.db = self.client[self.db_name][self.db_name]

    async def save_flood(
        self,
        chat_id: int,
        limit: int,
        within: int,
        action: str,
    ):
        with INSERTION_LOCK:
            curr = self.db.find_one({"chat_id": chat_id})
            if curr:
                if not (limit == int(curr['limit']) and within == int(curr['within']) and action == str(curr['action'])):
                    return self.db.update_one(
                        {"chat_id": chat_id},
                        {"$set": {
                            "limit": limit,
                            "within": within,
                            "action": action,
                        }}
                    )
                else:
                    return
            else:
                return self.db.insert_one(
                    {
                        "chat_id": chat_id,
                        "limit": limit,
                        "within": within,
                        "action": action
                    },
                )

    async def is_chat(self, chat_id: int):
        with INSERTION_LOCK:
            curr = self.db.find_one({"chat_id": chat_id})
            if curr:
                action = [str(curr['limit']), str(curr['within']), str(curr['action'])]
                return action
            return False

    async def get_action(self, chat_id: int):
        with INSERTION_LOCK:
            curr = self.db.find_one({"chat_id": chat_id})
            if curr:
                return curr['action']
            return "Flood haven't set"

    async def rm_flood(self, chat_id: int):
        with INSERTION_LOCK:
            curr = self.db.find_one({"chat_id": chat_id})
            if curr:
                self.db.delete_one({"chat_id": chat_id})
                return True
            return False


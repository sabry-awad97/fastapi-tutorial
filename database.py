from pymongo import MongoClient, collection
from bson import ObjectId
from typing import Any, Dict, Optional


class Database:
    _client: Optional[MongoClient] = None

    @classmethod
    def get_client(cls) -> MongoClient:
        if cls._client is None:
            cls._client = MongoClient("mongodb://localhost:27017/")
        return cls._client

    def __init__(self, collection_name: str):
        self.db = self.get_client()["store"]
        self.collection: collection.Collection = self.db[collection_name]

    def get_items(self) -> collection.Cursor:
        return self.collection.find({})

    def insert_item(self, item: Dict[str, Any]) -> collection.InsertOneResult:
        return self.collection.insert_one(item)

    def find_item(self, item_id: str) -> Optional[Dict[str, Any]]:
        return self.collection.find_one({"_id": ObjectId(item_id)})

    def update_item(
        self, item_id: str, item_data: Dict[str, Any]
    ) -> collection.UpdateResult:
        return self.collection.update_one(
            {"_id": ObjectId(item_id)}, {"$set": item_data}
        )

    def delete_item(self, item_id: str) -> collection.DeleteResult:
        return self.collection.delete_one({"_id": ObjectId(item_id)})

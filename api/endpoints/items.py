from fastapi import APIRouter, HTTPException, Body
from api.models.item import Item, ItemCreate
from pymongo import MongoClient
from bson import ObjectId

router = APIRouter()

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["store"]
collection = db["items"]


@router.get("/items/", response_model=list[Item])
async def get_items():
    """
    Get all items.
    """
    cursor = collection.find({})
    items = []
    for document in cursor:
        item_id = str(document["_id"])
        items.append({"id": item_id, **document})
    return items


@router.post("/items/", response_model=Item)
async def create_item(item: ItemCreate = Body(...)):
    """
    Create a new item without an ID.
    """
    inserted_item = collection.insert_one(item.model_dump())
    item_id = str(inserted_item.inserted_id)
    return {"id": item_id, **item.model_dump()}


@router.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    """
    Get an item by ID.
    """
    item = collection.find_one({"_id": ObjectId(item_id)})
    if item:
        return {"id": item_id, **item}
    raise HTTPException(status_code=404, detail="Item not found")


@router.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item = Body(...)):
    """
    Update an item by ID.
    """
    updated_item = collection.update_one(
        {"_id": ObjectId(item_id)}, {"$set": item.model_dump()}
    )
    if updated_item.modified_count:
        return {"id": item_id, **item.dict()}
    raise HTTPException(status_code=404, detail="Item not found")


@router.delete("/items/{item_id}")
async def delete_item(item_id: str):
    """
    Delete an item by ID.
    """
    deleted_item = collection.delete_one({"_id": ObjectId(item_id)})
    if deleted_item.deleted_count:
        return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")

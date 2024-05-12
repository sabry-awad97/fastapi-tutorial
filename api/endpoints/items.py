from api.models.item import Item, ItemCreate
from database import Database
from fastapi import APIRouter, HTTPException, Body, status
from pymongo.errors import PyMongoError

router = APIRouter()

# Establish a connection to the MongoDB database
db = Database("items")


@router.get("/items/", response_model=list[Item])
async def get_items():
    """
    Retrieve all items from the database.

    Returns:
        list[Item]: A list of items, each represented as an Item model.
    """
    try:
        cursor = db.get_items()
        items = []
        for document in cursor:
            item_id = str(document["_id"])
            items.append({"id": item_id, **document})
        return items
    except PyMongoError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@router.post("/items/", response_model=Item)
async def create_item(item: ItemCreate = Body(...)):
    """
    Create a new item in the database.

    Args:
        item (ItemCreate): The item data to create, excluding the ID.

    Returns:
        Item: The created item including its new unique identifier.
    """
    try:
        inserted_item = db.insert_item(item.model_dump())
        item_id = str(inserted_item.inserted_id)
        return {"id": item_id, **item.model_dump()}
    except PyMongoError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@router.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    """
    Retrieve a single item by its ID.

    Args:
        item_id (str): The unique identifier of the item.

    Returns:
        Item: The requested item if found.

    Raises:
        HTTPException: If no item is found with the provided ID.
    """
    try:
        item = db.find_item(item_id)
        if item:
            return {"id": item_id, **item}
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
            )
    except PyMongoError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@router.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item = Body(...)):
    """
    Update an existing item by its ID.

    Args:
        item_id (str): The unique identifier of the item to update.
        item (Item): The updated item data.

    Returns:
        Item: The updated item.

    Raises:
        HTTPException: If no item is found with the provided ID or if the update fails.
    """
    try:
        updated_item = db.update_item(item_id, item.model_dump())
        if updated_item.modified_count:
            return {"id": item_id, **item.model_dump()}
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
            )
    except PyMongoError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@router.delete("/items/{item_id}")
async def delete_item(item_id: str):
    """
    Delete an item by its ID.

    Args:
        item_id (str): The unique identifier of the item to delete.

    Returns:
        dict: A message indicating successful deletion.

    Raises:
        HTTPException: If no item is found with the provided ID or if the deletion fails.
    """
    try:
        db = Database("items")
        deleted_item = db.delete_item(item_id)
        if deleted_item.deleted_count:
            return {"message": "Item deleted successfully"}
        else:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
            )
    except PyMongoError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )

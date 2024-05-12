from pydantic import BaseModel


class ItemBase(BaseModel):
    """
    Base model for item data, used as a foundation for more specific item models.
    Attributes:
        name (str): The name of the item.
        price (float): The price of the item.
    """

    name: str
    price: float


class ItemCreate(ItemBase):
    """
    Data model for creating a new item, inherits from ItemBase.
    Currently, it does not add any additional fields to ItemBase.
    """

    pass


class Item(ItemBase):
    """
    Data model for an item, including its unique identifier.
    Attributes:
        id (str): The unique identifier for the item.
    """

    id: str

    class Config:
        """
        Configuration class for Pydantic model settings.
        """

        from_attributes = True  # Allows model initialization from attributes.

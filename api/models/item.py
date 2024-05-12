from pydantic import BaseModel


class ItemBase(BaseModel):
    name: str
    price: float


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: str

    class Config:
        from_attributes = True

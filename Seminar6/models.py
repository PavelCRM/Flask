from pydantic import BaseModel


class UserInDB(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str


class ItemInDB(BaseModel):
    id: int
    name: str
    description: str
    price: float


class ItemCreate(BaseModel):
    name: str
    description: str
    price: float


class OrderInDB(BaseModel):
    id: int
    user_id: int
    item_id: int
    order_date: str
    status: str


class OrderCreate(BaseModel):
    user_id: int
    item_id: int
    order_date: str
    status: str

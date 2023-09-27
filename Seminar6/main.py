from fastapi import FastAPI, HTTPException
from database import database, users, items, orders
from models import UserInDB, UserCreate, ItemInDB, ItemCreate, OrderInDB, OrderCreate
from typing import List

app = FastAPI()


# Маршруты
@app.post("/users/", response_model=UserInDB)
async def create_user(user: UserCreate):
    query = users.insert().values(**user.dict())
    user_id = await database.execute(query)
    return {**user.dict(), "id": user_id}


@app.get("/users/{user_id}", response_model=UserInDB)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    user = await database.fetch_one(query)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.post("/items/", response_model=ItemInDB)
async def create_item(item: ItemCreate):
    query = items.insert().values(**item.dict())
    item_id = await database.execute(query)
    return {**item.dict(), "id": item_id}


@app.get("/items/{item_id}", response_model=ItemInDB)
async def read_item(item_id: int):
    query = items.select().where(items.c.id == item_id)
    item = await database.fetch_one(query)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/orders/", response_model=OrderInDB)
async def create_order(order: OrderCreate):
    query = orders.insert().values(**order.dict())
    order_id = await database.execute(query)
    return {**order.dict(), "id": order_id}


@app.get("/orders/{order_id}", response_model=OrderInDB)
async def read_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    order = await database.fetch_one(query)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


# Запуск приложения
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

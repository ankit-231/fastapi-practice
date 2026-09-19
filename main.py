from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/users/me")
async def read_user_me():
    return "me"


# /users/me needs to be defined above /users/{user_id} since the latter also matches the former path and FastAPI always stops at the first path that matches.
@app.get("/users/{user_id}")
async def read_user_detail(user_id: int):
    return {"user_id": user_id}

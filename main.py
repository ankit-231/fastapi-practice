from enum import Enum

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


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


# this feature of using a path param (/home/ankit/abc.txt) is provided directly by Starlette
# the resulting endpoint for `/home/johndoe/myfile.txt` would be: `/files//home/johndoe/myfile.txt`, note the double slash `//`.
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

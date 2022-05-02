from enum import Enum
from typing import Optional

from fastapi import FastAPI

app = FastAPI()
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/")
async def root():
    return {"message": "This is Fast API in action"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return dict(model_name=model_name, message="Deep Learning FTW!")

    if model_name.value == "lenet":
        return dict(model_name=model_name, message="LeCNN all the images")

    return dict(model_name=model_name, message="Have some residuals")


# uvicorn rest_api.fast_api.main:app --reload
# https://fastapi.tiangolo.com/tutorial/path-params/#path-convertor
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

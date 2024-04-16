from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


app = FastAPI()


class Item(BaseModel):
    name: str
    description: str


@app.post("/items/")
async def create_item(item: Item):
    return item


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

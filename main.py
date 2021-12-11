# Put the code for your API here.



from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Value(BaseModel):
    value: int


@app.get("/")
async def welcome():
    return {"welcome!!"}

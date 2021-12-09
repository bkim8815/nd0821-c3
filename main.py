# Put the code for your API here.



from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Value(BaseModel):
    value: int


@app.get("/")
async def exercise_function(path: int, query: int, body: Value):
    return {"path": path, "query": query, "body": body}

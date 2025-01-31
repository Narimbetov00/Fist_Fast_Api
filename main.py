from fastapi import FastAPI,Depends
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
async def root():
    return {"message":"hello world"}


class MyModel(BaseModel):
    name : str
    description : str
    age : int

    class Config:
        schema_extra = {
            "example":{
                "name":"Foo",
                "description":"qwerty",
                "age":1
            }
        
        }


@app.post("/")
async def post(mymodel:MyModel):
    return mymodel



async def common_parameters(q:str|None=None,skip:int = 0, limit:int = 100):
    return {"q":q,"skip":skip,"limit":limit}

@app.get("/items/")
async def read_items(commons:dict=Depends(common_parameters)):
    return commons

@app.get("/users/")
async def read_users(commons:dict=Depends(common_parameters)):
    return commons


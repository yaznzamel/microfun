from fastapi import FastAPI
from api.routers import functions


app = FastAPI()

app.include_router(functions.router)

@app.get("/")
def read_root():
    return {"Message" : "Welcome to micronfun :) "}


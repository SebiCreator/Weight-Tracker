from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

database = {
    "data":[{"weight": 81.7, "date": 1675796142420},{"weight": 80, "date": 1675796134737}]
}

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/weights")
async def index():
    return database

@app.post("/weights")
async def addData(item):
    database["data"].append(item)
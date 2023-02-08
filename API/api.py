from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
import sqlite3 as sql

con = sql.connect("/Users/sebastiankaeser/Coding/weight-tracker/Database/weights.db")
cur = con.cursor()

def add_day_to_database(weight,timestamp):
    statement = f"INSERT INTO WEIGHTS VALUES ({weight} , '{timestamp}')"
    cur.execute(statement)
    con.commit()

def get_days_from_database(days=None):
    statement = f"SELECT * FROM WEIGHTS"
    res = cur.execute(statement)
    
    if res.fetchone() is None:
        return []
        
    res_output = res.fetchall()
    ret_val = []
    for weight, date in res_output:
       entry = {"weight": weight, "date": int(date)}
       ret_val.append(entry) 
    return ret_val

def moving_average(liste,window):
    output = []
    for idx in range(len((liste))):
       if idx < window:
           value = sum([liste[idx2] for idx2 in range(idx,-1,-1)])
           output.append(value) 
       else:
           value = sum([liste[idx2] for idx2 in range(window)]) / window
           output.append(value)
    return output

app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/days")
async def index():
    return {"result": get_days_from_database()}


@app.post("/day")
async def addData(weight,timestamp):
    print((weight,timestamp))
    add_day_to_database(weight,timestamp)
    return {
        "status": "sucess"
    }
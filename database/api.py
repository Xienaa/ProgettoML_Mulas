from fastapi import FastAPI
from secret import secretget_all

app = FastAPI()

@app.get("/shoptrends")
def get_all(): 
    all_data=secretget_all()   
    return all_data



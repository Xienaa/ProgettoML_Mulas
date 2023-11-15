from fastapi import FastAPI
from secret import secretget_all,secretdelete,secretadd,secretupdate

app = FastAPI()

@app.get("/shoptrends")
def get_all(): 
    all_data=secretget_all()   
    return all_data

@app.delete("/deletecustomer/{Customer_Id}")
def delete(Customer_Id: int):
    delete_user=secretdelete({Customer_Id})
    return delete_user

@app.post("/addcustomer")
def add():
    add_user=secretadd()
    return add_user

@app.put("/updatecustomer")
def update():
    update_user=secretupdate()
    return update_user


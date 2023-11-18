from fastapi import FastAPI
from secret import secretget_by_id,secretget_all,secretdelete,create_user_in_function,CustomerInput,secretupdate,CustomerUpdateInput

app = FastAPI()

@app.get("/shoptrends")
def get_all(): 
    all_data=secretget_all()   
    return all_data

@app.get("/shoptrendsbyid/{customer_id}")
def getbyid(customer_id: int): 
    select_data = secretget_by_id(customer_id)   
    return select_data

@app.delete("/deletecustomer/{customer_id}")
def delete(customer_id: int):
    delete_user=secretdelete({customer_id})
    return delete_user

@app.post("/createuser")
async def create_user_endpoint(customer_data: CustomerInput):
    return create_user_in_function(customer_data)

@app.put("/updateuser")
async def update_user_endpoint(update_data: CustomerUpdateInput):
    return secretupdate(update_data)(update_data)
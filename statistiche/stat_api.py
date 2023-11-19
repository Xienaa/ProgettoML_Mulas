from fastapi import FastAPI
from secret_stat import calculate_average_age_from_db

app = FastAPI()

@app.get("/average_age")
async def calculate_average_age_endpoint():
    average_age = calculate_average_age_from_db()
    return {"average_age": average_age}
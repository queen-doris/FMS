from fastapi import FastAPI
from app.routers import fleet
from app.database import engine
from app.models import Base

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(fleet.router)

@app.get("/")
def root():
    return {"message": "Welcome to Fleet Management System!"}

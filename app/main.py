from fastapi import FastAPI, Depends
from app.api.routers import users


app = FastAPI()

app.include_router(users.router)

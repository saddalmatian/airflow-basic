from app.models.schemas import user as user_schemas
from app.db import user as user_db


def create_user(user: user_schemas.UserIn):
    return user_db.create_user(user)


def get_user(username:str):
    return user_db.get_user(username)
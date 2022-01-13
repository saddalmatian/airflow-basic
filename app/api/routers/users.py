from fastapi import APIRouter
from app.models.schemas import user as user_schema
from app.services import user as user_service


router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


@router.post("/create-user")
def create_user(user: user_schema.UserIn):
    return user_service.create_user(user)


@router.get("/{user_name}")
def get_user(user_name: str):
    return user_service.get_user(user_name)

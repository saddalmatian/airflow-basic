from pydantic import BaseModel
from pydantic.fields import Field


class User(BaseModel):
    username:str = Field(...,alias="Username")


class UserInDB(User):
    created_at:str = Field(...,alias="CreatedAt")
    organization:dict = Field(...,alias="Organization")
    type:str = Field(...,alias="Type")

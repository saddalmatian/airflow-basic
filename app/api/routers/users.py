from fastapi import APIRouter, Depends, HTTPException
from app.models.schemas import user as user_schema
from app.services import user as user_service
from fastapi.security import OAuth2PasswordBearer
from pydantic import ValidationError
from typing import Union, Any
from datetime import datetime, timedelta
import jwt
from fastapi.security import HTTPBearer


SECURIT_ALGORITHM = 'HS256'
SECRET_KEY = '123456'

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(username, password):
    if username == 'admin' and password == 'admin':
        return True
    return False


def generate_token(username: Union[str, Any]) -> str:
    expire = datetime.utcnow() + timedelta(
        seconds=60 * 60 * 24 * 3  # Expired after 3 days
    )
    to_encode = {
        "exp": expire, "username": username
    }
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY,
                             algorithm=SECURIT_ALGORITHM)
    # First para is payload

    return encoded_jwt


reusable_oauth2 = HTTPBearer(
    scheme_name='Authorization'
)


def validate_token(credentials=Depends(reusable_oauth2)) -> str:
    """
    Decode JWT token
    """
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY,
                             algorithms=[SECURIT_ALGORITHM])
        if payload.get('exp') < datetime.utcnow().timestamp():
            raise HTTPException(status_code=403, detail="Token expired")
    except(jwt.PyJWTError, ValidationError):
        raise HTTPException(
            status_code=403, detail="Could not validate credentials")


@router.post("/create-user")
def create_user(user: user_schema.UserIn):
    return user_service.create_user(user)


@router.get("/{user_name}", dependencies=[Depends(validate_token)])
def get_user(user_name: str, token=Depends(oauth2_scheme)):
    return user_service.get_user(user_name)


@router.post('/login')
def login(username: str, password: str):
    if verify_password(username, password):
        token = generate_token(username)
        return {
            'token': token
        }
    else:
        raise HTTPException(status_code=404, detail="User not found")

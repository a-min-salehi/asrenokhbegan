from typing import Optional
from pydantic import BaseModel
from enum import Enum


class Role(str, Enum):
    user = "user"
    admin = "admin"
    vip = "vip"


class User(BaseModel):
    id: Optional[str]
    username: str
    roles: Role
    password: str


class UserUpdate(BaseModel):
    username: Optional[str]
    roles: Optional[Role]
    password: Optional[str]


class TokenData(BaseModel):
    username: Optional[str] = None


class Login(BaseModel):
    username: str
    password: str

from pydantic import BaseModel
from typing import Optional
from enum import Enum


class Role(str, Enum):
    user = "user"
    admin = "admin"
    vip = "vip"


class User(BaseModel):
    id: Optional[int]
    email: str
    password: str
    roles: Role


class UserUpdateRequest(BaseModel):
    email: Optional[str]
    password: Optional[str]
    roles: Optional[Role]

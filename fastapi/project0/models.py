from pydantic import BaseModel
from typing import Optional, List
from enum import Enum
from uuid import UUID, uuid4


class Gender(str, Enum):
    male = "male"
    female = "female"
    custom = "custom"


class Role(str, Enum):
    user = "user"
    admin = "admin"
    vip = "vip"


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    full_name: str
    gender: Gender
    roles: List[Role]


class UserUpdateRequest(BaseModel):
    full_name: Optional[str]
    gender: Optional[Gender]
    roles: Optional[List[Role]]

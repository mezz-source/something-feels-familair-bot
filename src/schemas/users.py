from typing import Any
from pydantic import BaseModel

class CreateUser(BaseModel):
    username: str
    password: str

class ModifyUser(BaseModel):
    modifications: dict[str, Any]

class LoginUser(BaseModel):
    username: str
    password: str
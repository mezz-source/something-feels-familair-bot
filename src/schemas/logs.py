from typing import Any

from pydantic import BaseModel
from datetime import datetime

class CreateLog(BaseModel):
    date: datetime
    author: str
    message: str

class ModifyLog(BaseModel):
    modifications: dict[str, Any]
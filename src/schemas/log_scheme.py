from datetime import datetime

from pydantic import BaseModel

class CreateLog(BaseModel):
    message: str
    created_at: datetime | None = None

class ModifyLog(BaseModel):
    message: str | None = None

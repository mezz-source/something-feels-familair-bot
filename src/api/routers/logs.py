from fastapi import APIRouter
from src.schemas.logs import CreateLog, ModifyLog

router = APIRouter(prefix="/logs")

@router.get("/{log_id}")
async def get_log(log_id: int):
    return {"log_id": log_id, "author": f"author{log_id}", "message": f"log message {log_id}"}

@router.post("/")
async def create_log(log: CreateLog):
    return {"author": log.author, "message": log.message, "date": log.date, "message": "Log created successfully"}

@router.patch("/{log_id}")
async def modify_log(log_id: int, modifications: ModifyLog):
    return {"log_id": log_id, "modifications": modifications.modifications, "message": "Log modified successfully"}

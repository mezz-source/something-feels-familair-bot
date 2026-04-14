from fastapi import APIRouter
from src.schemas.users import CreateUser, ModifyUser, LoginUser

router = APIRouter(prefix="/users")

@router.get("/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id, "username": f"user{user_id}"}

@router.post("/")
async def create_user(user: CreateUser):
    return {"username": user.username, "message": "User created successfully"}

@router.delete("/{user_id}")
async def delete_user(user_id: int):
    return {"user_id": user_id, "message": "User deleted successfully"}

@router.patch("/{user_id}")
async def update_user(user_id: int, modifications: ModifyUser):
    return {"user_id": user_id, "modifications": modifications.modifications, "message": "User updated successfully"}

@router.post("/login")
async def login(login: LoginUser):
    return {"username": login.username, "message": "Login successful"}
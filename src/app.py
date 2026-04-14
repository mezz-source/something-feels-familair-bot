from fastapi import FastAPI
from src.api.routers.users import router as users_router
from src.api.routers.logs import router as logs_router
app = FastAPI(prefix="/api")
app.include_router(users_router)
app.include_router(logs_router)

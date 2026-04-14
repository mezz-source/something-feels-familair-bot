from pathlib import Path

from fastapi import APIRouter
from starlette.responses import FileResponse

router = APIRouter(prefix="/secrets")

BOOM_VIDEO_PATH = Path(__file__).resolve().parents[3] / "assets" / "boom.mp4"

@router.get("/boom")
async def boom():
    return FileResponse(
        BOOM_VIDEO_PATH,
        media_type="video/mp4",
        headers={"Content-Disposition": 'inline; filename="boom.mp4"'},
    )

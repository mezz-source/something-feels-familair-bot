from pathlib import Path

from fastapi import APIRouter, Request
from starlette.responses import FileResponse
from fastapi.responses import JSONResponse

from src.security.rate_limit import limiter

router = APIRouter(prefix="/secrets")

BOOM_VIDEO_PATH = Path(__file__).resolve().parents[3] / "assets" / "boom.mp4"
YOU_NEED_ME_AUDIO_PATH = Path(__file__).resolve().parents[3] / "assets" / "youneedme.mp3"

@router.get("/boom")
@limiter.limit("20/minute")
async def boom(request: Request):
    return FileResponse(
        BOOM_VIDEO_PATH,
        media_type="video/mp4",
        headers={"Content-Disposition": 'inline; filename="boom.mp4"'},
    )

@router.get("/you-need_me")
@limiter.limit("20/minute")
async def dr_breen_again(request: Request):
    return FileResponse(
        YOU_NEED_ME_AUDIO_PATH,
        media_type="audio/mp3",
        headers={"Content-Disposition": 'inline; filename="youneedme.mp3"'},
    )


@router.get("/mezz-note")
@limiter.limit("20/minute")
async def mezz_note(request: Request):
    return JSONResponse(
        {
            "secret": "solving syntax errors since 1998",
            "credit": "mezz_inc",
        }
    )

# it helped me with the websocket implementation 💗
@router.get("/copilot-note")
@limiter.limit("20/minute")
async def copilot_note(request: Request):
    return JSONResponse(
        {
            "secret": "If you're reading this, the logs are whispering back.",
            "credit": "Added by GitHub Copilot (GPT-5.3-Codex)",
        }
    )

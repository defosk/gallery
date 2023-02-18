import io
from functools import lru_cache
from pathlib import Path
from PIL import Image
from fastapi import Depends, FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse, StreamingResponse
from generate import create
from config import Settings


@lru_cache()
def get_settings():
    return Settings()


app = FastAPI()
BASE_DIR = Path.cwd()

app.mount("/img", StaticFiles(directory=get_settings().IMAGE_DIR, html=True), name="index")
app.mount("/static", StaticFiles(directory=f"{BASE_DIR}/public", html=True), name="static")


@app.get("/")
async def read_index(settings: Settings = Depends(get_settings)):
    create(settings.IMAGE_DIR)
    return FileResponse(f'{settings.IMAGE_DIR}/index.html')


@app.get("/preview")
async def preview(img_path: str, settings: Settings = Depends(get_settings)):
    image = Image.open(f'{settings.IMAGE_DIR}/{img_path}')
    image.thumbnail((220, 220))
    imgio = io.BytesIO()
    image = image.convert('RGB')
    image.save(imgio, 'JPEG')
    imgio.seek(0)
    return StreamingResponse(content=imgio, media_type="image/jpeg")

from fastapi import FastAPI, UploadFile, File, Form
from typing import List

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Backend OK!"}

@app.post("/generate-video")
async def generate_video(
    image_folder: str = Form(...),
    files: List[UploadFile] = File(None)
):
    return {
        "status": "received",
        "folder": image_folder,
        "files": [file.filename for file in files] if files else []
    }

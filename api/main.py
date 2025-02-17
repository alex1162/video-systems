from fastapi import FastAPI, UploadFile
from fastapi.responses import HTMLResponse
import api.P4 as P4

app = FastAPI()

# SHARED_FOLDER = "/shared"
MEDIA_FOLDER = "/media"

@app.get('/', response_class=HTMLResponse)
def home():
    html = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Home</title>
        </head>
        <body>
            <h1>Practice 1 - API & Dockerization</h1>
            <p> To test the endpoints implemented, go to the API docs page:</p>
            <button onclick="window.location.href='/docs';">Go</button>
        </body>
    </html>
    """
    return html

@app.post("/MP4_video")
async def MP4_video(file: UploadFile):
        
        input_path = f"{MEDIA_FOLDER}/{file.filename}"
        output_path = f"{MEDIA_FOLDER}/converted_{file.filename}.mp4"

        P4.MP4_video(input_path, output_path, docker)

        return {"status": "success", "output_file": output_path}

@app.post("/MKV_video")
async def MKV_video(file: UploadFile):
        
        input_path = f"{MEDIA_FOLDER}/{file.filename}"
        output_path = f"{MEDIA_FOLDER}/converted_{file.filename}.mkv"

        P4.MKV_video(input_path, output_path, docker)

        return {"status": "success", "output_file": output_path}

@app.post("/cut_video")
async def cut_video(file: UploadFile):
        
        input_path = f"{MEDIA_FOLDER}/{file.filename}"
        output_path = f"{MEDIA_FOLDER}/cut_{file.filename}"

        P4.cut_video(input_path, output_path, docker)

        return {"status": "success", "output_file": output_path}
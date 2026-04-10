from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response
from rembg import remove

app = FastAPI()

@app.post("/remove-bg")
async def remove_background(file: UploadFile = File(...)):
    contents = await file.read()
    result = remove(contents)
    return Response(content=result, media_type="image/png")
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import Response, JSONResponse
from rembg import new_session, remove

app = FastAPI()
session = None

@app.on_event("startup")
def load_model():
    global session
    session = new_session("u2net")

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/remove-bg")
async def remove_background(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        result = remove(contents, session=session)
        return Response(content=result, media_type="image/png")
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post("/files/")
async def login(file: UploadFile=File(...)):
    content = await file.read()
    size_bytes = len(content)
    return {'file_size': size_bytes}

@app.post("/uploadfile/")
async def login(file: UploadFile=File(...)):
    return {'filename': file.filename}
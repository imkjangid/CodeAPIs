# app.py
from fastapi import FastAPI
import asyncio, httpx

app = FastAPI()

@app.get("/hello")
async def hello():
    return {"message": "Hello CodeAPIs!"}


@app.get("/wait/{seconds}")
async def wait(seconds: float):
    # non-blocking sleep
    await asyncio.sleep(seconds)
    return {"waited": seconds}


@app.get("/external/{id}")
async def external(id: int):
    # non-blocking HTTP call using httpx.AsyncClient
    url = f"https://dummyjson.com/todos/{id}"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()
        return resp.json()
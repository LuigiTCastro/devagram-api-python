from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from routes.UserRoute import router as UserRoute



app = FastAPI()

app.include_router(UserRoute, tags=['User'], prefix='/api/user')


@app.get('/api/health', tags=['Health'])
async def health():
    return {
        'status': '200 OK'
    }
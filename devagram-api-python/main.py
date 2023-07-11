from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    password: str
    description: Optional[str] = None


app = FastAPI()

@app.get('/health')
async def health():
    return {
        'status': '200 OK'
    }


@app.post('/login')
async def login(user:User):
    if user.email == 'xx' and user.password == 'yy':
        # return {
        #     'status': 'Login successfully realized.'
        # }

        return 'Login successfully realized.'
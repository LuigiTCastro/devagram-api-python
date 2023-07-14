from models.UserModel import UserLoginModel
from services.AuthService import login_service
from fastapi import APIRouter, Body, HTTPException

router = APIRouter()

@router.post('/login', response_description='Login')
async def login_route(user: UserLoginModel = Body(...)):
    result = await login_service(user)
    
    if not result['status'] == 200:
        raise HTTPException(status_code=result['status'], detail=result['message'])
    
    return result
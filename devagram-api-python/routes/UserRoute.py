from fastapi import APIRouter, Body
from models.UserModel import UserModel
from repositories.UserRepository import createUser

router = APIRouter()

@router.post('/', response_description= 'Route to create a new user.')
async def registerUser(user: UserModel = Body(...)):
    result = await createUser(user)
    return result
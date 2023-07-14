from fastapi import APIRouter, Body, HTTPException
from models.UserModel import UserCreateModel
from services.UserService import UserService

router = APIRouter()

@router.post('/', response_description= 'Route to create a new user.')
async def registerUser(user: UserCreateModel = Body(...)):
    try:
        result = await UserService.registerUser(user)
        
        if not result['status'] == 201:
            raise HTTPException(status_code=result['status'], detail=result['message'])
            # raise (python) = throw (js)
        
        return result
    
    except Exception as error:
        print(error)
        return {
            'message': 'Server internal error.'
        }
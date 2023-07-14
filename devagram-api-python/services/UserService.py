from models.UserModel import UserCreateModel
from repositories.UserRepository import UserRepository 


class UserService:

    async def registerUser(user: UserCreateModel):
        try:
            user = await UserRepository.findUserByEmail(user.email)

            if user:
                return {
                    'message': 'User already exists.',
                    'data': '',
                    'status': 400
                }
            
            else:
                new_user = await UserRepository.createUser(user)
                return {
                    'message': 'User successfully registered.',
                    'data': new_user,
                    'status': 201
                }
            
        except Exception as error:
            return {
                'message': 'Internal server error.',
                'data': str(error),
                'status': 500
            }

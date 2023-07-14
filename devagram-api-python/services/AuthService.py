from models.UserModel import UserLoginModel
from repositories.UserRepository import UserRepository
from utils.AuthUtil import AuthUtil

class AuthService:
    
    async def login_service(user: UserLoginModel):
        
        try:
            wanted_user = await UserRepository.findUserByEmail(user.email)
            
            if not wanted_user:
                return {
                    'message': 'User not found.',
                    'data': '',
                    'status': 401
                }
            
            
            if AuthUtil.decrypt_password(user.password, wanted_user.password):
                return {
                    'message': 'Login successfully realized.',
                    'data': wanted_user,
                    'status': 200
                }
                
            else:
                return {
                    'message': 'User not found.',
                    'data': '',
                    'status': 401
                }
        
        except Exception as error:
            print(error)
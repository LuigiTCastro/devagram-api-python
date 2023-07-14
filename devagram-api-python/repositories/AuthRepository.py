

class AuthRepository:
    
    def login_repository(user: UserLoginModel):
        
        try:
            user = user_collection.find_one({'email': user.email})
            
            if not user:
                print('User not found.')
                
            
        
        except Exception as error:
            print(error)
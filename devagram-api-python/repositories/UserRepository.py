import motor.motor_asyncio
from decouple import config
from bson import ObjectId
from models.UserModel import UserCreateModel
from services.AuthService import AuthService
# from utils.userHelper import userHelper

def userHelper(user):
    return {
        'id': user['_id'],
        'name': user['name'],
        'email': user['email'],
        'password': user['password'],
        'photo': user['photo'],
    }

MONGODB_URL = config('MONGODB_URL')

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
database = client.devagrampythoncluster
user_collection = database.get_collection('user')


class UserRepository:

    async def createUser(user:UserCreateModel) -> dict:
        user.password = AuthService.encrypt_password(user.password)
        user_created = await user_collection.insert_one(user.__dict__)
        new_user = await user_collection.find_one({ '_id': user_created.inserted_id })

        return userHelper(new_user)
        # return {
        #     'id': str(user['_id']),
        #     'name': user['name'],
        #     'email': user['email'],
        #     'password': user['password'],
        #     'photo': user['photo'],
        # }


    async def listUsers():
        return user_collection.find()


    async def findUserByEmail(email: str):
        user = user_collection.find_one({'email': email})

        if not user:
            print('user not found')
        
        return userHelper(user)


    async def findUserById():
        pass


    async def updateUser(id: str, user_data: dict):
        user = await user_collection.find_one({"_id": ObjectId(id)})

        
        if user:
            updated_user = await user_collection.update_one(
                {"_id": ObjectId(id)}, {"$set": user_data}
            )

        return userHelper(updated_user)


    async def deleteUser(id: str):
        user = await user_collection.find_one({"_id": ObjectId(id)})

        if not user:
            print('user not found')

        await user_collection.delete_one({"_id": ObjectId(id)})
from pydantic import BaseModel, Field, EmailStr


class UserModel(BaseModel):
    id: str = Field(...)
    name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    photo: str = Field(...)

    class Config:
        schema_extra = {
            'user': {
                'name': 'fulano',
                'email': 'fulano@email.com',
                'password': 'password123',
                'photo': 'photo.png'
            }
        }


class UserCreateModel(BaseModel):
    name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    photo: str = Field(...)

    class Config:
        schema_extra = {
            'user': {
                'name': 'fulano',
                'email': 'fulano@email.com',
                'password': 'password123',
                'photo': 'photo.png'
            }
        }


class UserLoginModel(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        schema_extra = {
            'user': {
                'email': 'fulano@email.com',
                'password': 'password123',
            }
        }
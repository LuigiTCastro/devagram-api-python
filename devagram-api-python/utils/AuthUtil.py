from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'])

class AuthUtil:
    def encrypt_password(password):
        return pwd_context.hash(password)

    def decrypt_password(password, encryptedPassowrd):
        return pwd_context.verify(password, encryptedPassowrd)
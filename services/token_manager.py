import base64
from cryptography.fernet import Fernet

class TokenManager:
    @staticmethod
    def encrypt_token(token: str, key: str | bytes) -> str:
        if type(key) == str:
            key = base64.urlsafe_b64decode(key)
        cipher = Fernet(key)
        return cipher.encrypt(token.encode()).decode()

    @staticmethod
    def decrypt_token(encrypted_token: str, key: str | bytes) -> str:
        if type(key) == str:
            key = base64.urlsafe_b64decode(key)
        cipher = Fernet(key)
        return cipher.decrypt(encrypted_token.encode()).decode()
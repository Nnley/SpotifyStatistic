from cryptography.fernet import Fernet

class TokenManager:
    @staticmethod
    def encrypt_token(token: str, key: bytes) -> str:
        cipher = Fernet(key)
        return cipher.encrypt(token.encode()).decode()

    @staticmethod
    def decrypt_token(encrypted_token: str, key: bytes) -> str:
        cipher = Fernet(key)
        return cipher.decrypt(encrypted_token.encode()).decode()
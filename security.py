from passlib.context import CryptContext

pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
)

def encryptPassword(password):
    return pwd_context.hash(password)

def checkEncryptedPassword(password, hashed):
    return pwd_context.verify(password, hashed[:-1])

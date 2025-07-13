import bcrypt
import jwt
from datetime import datetime, timedelta
import sqlite3

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt(rounds=14)
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(
        plain_password.encode('utf-8'),
        hashed_password.encode('utf-8')
    )

def generate_jwt_token(username: str) -> str:
    payload = {
        'sub': username,
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(hours=2)
    }
    return jwt.encode(
        payload,
        st.secrets["JWT_SECRET_KEY"],
        algorithm="HS256"
    )
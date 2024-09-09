from datetime import datetime,timezone,timedelta
from jose import JWTError,jwt
from .. import schemas

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30





#picked from documentations

def create_access_token(data: dict):
    to_encode = data.copy()
    # if expires_delta:
    #     expire = datetime.now(timezone.utc) + expires_delta
    # else:
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)    # {'sub': ; value, 'exp':'value'}
    return encoded_jwt

def verify_token(token:str, credentials_exception):
    try:
        payload =  jwt.decode(token,SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except JWTError as e:
        print(f"Token verification failed: {e}")
        raise credentials_exception

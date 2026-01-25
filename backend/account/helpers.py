from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from tools.util import datetime_now, generate_token


# Validate token and return the spesific user
def get_user(
    request: Request,
    credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
) -> dict:
    token = credentials.credentials
    # Access app.state.USERS via request
    users = request.app.state.USERS
    # Find user by token
    user = next((u for u, v in users.items() if v["token"] == token), None)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        )
    return {"user": user}


def read_user(username: str, request: Request) -> dict:
    users = request.app.state.USERS
    print()
    print(users)
    print(username)
    print(users[username])
    print()
    if username not in users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return users[username]


def gen_user(username: str) -> dict:
    user = {
        "username": username,
        "token": generate_token(),
        "registered": datetime_now(),
        "x": 0,
        "y": 0,
        "z": 0,
    }
    return user

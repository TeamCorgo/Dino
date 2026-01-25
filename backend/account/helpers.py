from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from tools.util import datetime_now, generate_token


# Validate token and return the spesific user
def get_user(
    request: Request,
    credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
) -> dict:
    access_token = credentials.credentials

    # Access stored users from app state
    users_by_username = request.app.state.USERS

    # Find the username that matches the provided token
    username = next(
        (
            username
            for username, user_data in users_by_username.items()
            if user_data["token"] == access_token
        ),
        None,
    )

    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )
    return request.app.state.USERS[username]
    # return {"user": username}


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

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from tools.state import User, state
from tools.util import generate_token


# Validate token and return the spesific user
def get_user(
    credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
) -> User:
    access_token = credentials.credentials

    # Find the user that matches the provided token
    user = next(
        (user for user in state.users.values() if user.token == access_token),
        None,
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )

    return user


def gen_user(username: str) -> User:
    return User(username=username, token=generate_token())

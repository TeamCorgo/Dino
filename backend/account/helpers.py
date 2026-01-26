import secrets

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from tools.state import User, state


# Generate a random token
def generate_token() -> str:
    return secrets.token_hex(16)  # 32-character hex token


# Validate token and return the spesific user
def get_user(
    credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
) -> User:
    access_token = credentials.credentials

    # Find the username that matches the provided token
    username = next(
        (user for user, token in state.tokens.items() if token == access_token),
        None,
    )

    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )

    return state.users[username]


def gen_user(username: str) -> User:
    state.tokens[username] = generate_token()
    return User(username=username)

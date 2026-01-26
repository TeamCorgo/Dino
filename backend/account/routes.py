from account.helpers import gen_user, get_user
from fastapi import APIRouter, Depends, HTTPException, status
from tools.state import User, state
from tools.util import username_shield

account_router = APIRouter()


@account_router.get("/protected")
def protected_route(user: User = Depends(get_user)) -> dict:
    return {
        "message": f"Hello {user.username}, you have accessed a protected route!",
    }


# Registration route
@account_router.post("/register")
def register(username: str) -> dict:
    # Username must be A-Z, a-z, 0-9 (limit to 16 chars)
    if not username_shield(username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid username. Only A-Z, a-z, 0-9 allowed, max 16 chars.",
        )
    print(state.users)

    # Cannot be already registered
    if username in state.users:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists",
        )

    state.users[username] = gen_user(username)
    print(state.users)
    print(state.tokens)
    return {"token": state.tokens[username]}

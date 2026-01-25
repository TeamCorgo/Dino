from account.helpers import gen_user, get_user
from fastapi import APIRouter, Depends, HTTPException, Request, status
from tools.util import username_shield

account_router = APIRouter()


@account_router.get("/protected")
def protected_route(user: dict = Depends(get_user), request: Request = None) -> dict:
    return {
        "message": f"Hello {user['username']}, you have accessed a protected route!",
    }


# Registration route
@account_router.post("/register")
def register(username: str, request: Request = None) -> dict:
    # Username must be A-Z, a-z, 0-9 (limit to 16 chars)
    if not username_shield(username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid username. Only A-Z, a-z, 0-9 allowed, max 16 chars.",
        )
    print(request.app.state.USERS)
    # Cannot be already registered
    if username in request.app.state.USERS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists",
        )

    request.app.state.USERS[username] = gen_user(username)
    print(request.app.state.USERS)
    return {"token": request.app.state.USERS[username]["token"]}

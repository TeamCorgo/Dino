from account.helpers import get_user
from fastapi import APIRouter, Depends, Request

map_router = APIRouter()


@map_router.get("/overview")
def map_overview(user: dict = Depends(get_user), request: Request = None) -> dict:
    return {
        "message": f"Hello {user['username']}, you have accessed a protected route!",
    }

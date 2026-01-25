from account.helpers import get_user
from fastapi import APIRouter, Depends
from tools.state import User
from world.helpers import user_view

action_router = APIRouter()


@action_router.post("/move_north")
def move_north(user: User = Depends(get_user)) -> dict:
    user.y += 1
    view = user_view(
        x=user.x,
        y=user.y,
        z=user.z,
    )
    return {"message": "Moved north", "view": view}


@action_router.post("/move_south")
def move_south(user: User = Depends(get_user)) -> dict:
    user.y -= 1
    view = user_view(
        x=user.x,
        y=user.y,
        z=user.z,
    )
    return {"message": "Moved south", "view": view}


@action_router.post("/move_east")
def move_east(user: User = Depends(get_user)) -> dict:
    user.x += 1
    view = user_view(
        x=user.x,
        y=user.y,
        z=user.z,
    )
    return {"message": "Moved east", "view": view}


@action_router.post("/move_west")
def move_west(user: User = Depends(get_user)) -> dict:
    user.x -= 1
    view = user_view(
        x=user.x,
        y=user.y,
        z=user.z,
    )
    return {"message": "Moved west", "view": view}

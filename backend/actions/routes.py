from account.helpers import get_user
from fastapi import APIRouter, Depends, Request

from backend.world.helpers import user_view

action_router = APIRouter()


@action_router.post("/move_north")
def move_north(user: dict = Depends(get_user), request: Request = None) -> dict:
    user["y"] += 1
    view = user_view(
        seed=request.app.state.CONFIG["seed"],
        theme=request.app.state.THEME[user["z"]],
        x=user["x"],
        y=user["y"],
        z=user["z"],
    )
    return {"message": "Moved north", "view": view}


@action_router.post("/move_south")
def move_south(user: dict = Depends(get_user), request: Request = None) -> dict:
    user["y"] -= 1
    view = user_view(
        seed=request.app.state.CONFIG["seed"],
        theme=request.app.state.THEME[user["z"]],
        x=user["x"],
        y=user["y"],
        z=user["z"],
    )
    return {"message": "Moved south", "view": view}


@action_router.post("/move_east")
def move_east(user: dict = Depends(get_user), request: Request = None) -> dict:
    user["x"] += 1
    view = user_view(
        seed=request.app.state.CONFIG["seed"],
        theme=request.app.state.THEME[user["z"]],
        x=user["x"],
        y=user["y"],
        z=user["z"],
    )
    return {"message": "Moved east", "view": view}


@action_router.post("/move_west")
def move_west(user: dict = Depends(get_user), request: Request = None) -> dict:
    user["x"] -= 1
    view = user_view(
        seed=request.app.state.CONFIG["seed"],
        theme=request.app.state.THEME[user["z"]],
        x=user["x"],
        y=user["y"],
        z=user["z"],
    )
    return {"message": "Moved west", "view": view}

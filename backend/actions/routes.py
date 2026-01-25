from account.helpers import get_user, read_user
from fastapi import APIRouter, Depends, Request
from tools.util import gen_color
from tools.world import user_view

action_router = APIRouter()


@action_router.post("/move_north")
def move_north(user: dict = Depends(get_user), request: Request = None) -> dict:
    request.app.state.USERS[user["user"]]["y"] += 1
    return {
        "message": "Moved north",
    }


@action_router.post("/move_south")
def move_south(user: dict = Depends(get_user), request: Request = None) -> dict:
    request.app.state.USERS[user["user"]]["y"] -= 1
    return {
        "message": "Moved south",
    }


@action_router.post("/move_east")
def move_east(user: dict = Depends(get_user), request: Request = None) -> dict:
    request.app.state.USERS[user["user"]]["x"] += 1
    color = gen_color(
        seed=request.app.state.CONFIG["seed"],
        theme=request.app.state.THEME[request.app.state.USERS[user["user"]]["z"]],
        x=request.app.state.USERS[user["user"]]["x"],
        y=request.app.state.USERS[user["user"]]["y"],
        z=request.app.state.USERS[user["user"]]["z"],
    )
    return {"message": "Moved east", "color": color}


@action_router.post("/move_west")
def move_west(username: dict = Depends(get_user), request: Request = None) -> dict:
    user = read_user(username["user"], request)
    user["x"] -= 1
    view = user_view(
        seed=request.app.state.CONFIG["seed"],
        theme=request.app.state.THEME[user["z"]],
        x=user["x"],
        y=user["y"],
        z=user["z"],
    )
    return {"message": "Moved west", "view": view}

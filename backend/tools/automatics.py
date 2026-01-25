from account.helpers import gen_user
from fastapi import FastAPI


def startup(app: FastAPI) -> None:
    print("⚙️ Startup")
    app.state.USERS["Hunter"] = gen_user("Hunter")
    app.state.USERS["Hunter"]["token"] = "asd"
    print(app.state.USERS)

    app.state.THEME[0] = ["#000000", "#FFFFFF"]
    print(app.state.THEME)
    return


def shutdown(app: FastAPI) -> None:
    print("⚙️ Shutdown")
    return

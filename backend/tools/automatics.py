from account.helpers import gen_user
from tools.state import state


def startup() -> None:
    print("⚙️ Startup")
    state.users["Hunter"] = gen_user("Hunter")
    state.users["Hunter"].token = "asd"
    print(state.users)

    state.themes[0] = ["#000000", "#FFFFFF"]
    print(state.themes)
    return


def shutdown() -> None:
    print("⚙️ Shutdown")
    return

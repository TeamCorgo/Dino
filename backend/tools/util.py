import random
import re
from datetime import datetime

from tools.state import Cell, state


def datetime_now() -> str:
    return datetime.now().strftime("%Y.%m.%d %H:%M")


def username_shield(username: str) -> bool:
    regex = re.compile(r"^[A-Za-z0-9]{1,16}$")
    return regex.match(username)


def gen_cord(x: int, y: int, z: int) -> str:
    return f"{str(x)}:{str(y)}:{str(z)}"


def gen_color(x: int, y: int, z: int) -> None:
    rng = random.Random(state.seed + ":" + gen_cord(x, y, z))
    cell = Cell(color=rng.choice(state.themes[z]))
    state.worlds[gen_cord(x, y, z)] = cell
    return

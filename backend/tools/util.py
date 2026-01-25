import random
import re
import secrets
from datetime import datetime


# Generate a random token
def generate_token() -> str:
    return secrets.token_hex(16)  # 32-character hex token


def datetime_now() -> str:
    return datetime.now().strftime("%Y.%m.%d %H:%M")


def username_shield(username: str) -> bool:
    regex = re.compile(r"^[A-Za-z0-9]{1,16}$")
    return regex.match(username)


def gen_color(seed: str, theme: list, x: int, y: int, z: int) -> str:
    rng = random.Random(seed + ":" + str(x) + ":" + str(y) + ":" + str(z))
    return rng.choice(theme)

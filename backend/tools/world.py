from tools.util import gen_color


def world_view(seed: str, theme: list, x: int, y: int, z: int, size: int) -> list:
    view = []
    for row in range(size):  # top → bottom (y)
        for col in range(size):  # left → right (x)
            # TODO check of overide first
            view.append(gen_color(seed, theme, x + col, y + row, z))
    return view


def user_view(seed: str, theme: list, x: int, y: int, z: int) -> list:
    view = []
    for row in range(5):  # top → bottom (y)
        for col in range(5):  # left → right (x)
            # TODO check of overide first
            view.append(gen_color(seed, theme, x + col, y + row, z))
    return view

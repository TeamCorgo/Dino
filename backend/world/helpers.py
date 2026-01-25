from tools.state import state
from tools.util import gen_color, gen_cord


def world_view(x: int, y: int, z: int, size: int) -> list:
    view = []
    for row in range(size):  # top → bottom (y)
        for col in range(size):  # left → right (x)
            cord = gen_cord(x + col, y + row, z)
            # check if cell doesnt exists in world
            if gen_cord(x + col, y + row, z) not in state.worlds:
                # Generate the cell
                state.worlds[cord] = gen_color(x + col, y + row, z)
            # read the cell from world
            view.append(state.worlds[cord].color)

    return view


def user_view(x: int, y: int, z: int) -> list:
    view = []
    for row in range(5):  # top → bottom (y)
        for col in range(5):  # left → right (x)
            cord = gen_cord(x + col, y + row, z)
            # check if cell doesnt exists in world
            if gen_cord(x + col, y + row, z) not in state.worlds:
                # Generate the cell
                gen_color(x + col, y + row, z)
            # read the cell from world
            view.append(state.worlds[cord].color)
    return view

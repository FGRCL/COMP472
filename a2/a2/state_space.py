from a2.position import Position
import copy


def successors(state, current_position: Position):
    height = len(state)
    width = len(state[0])

    if at_vertical_edge(current_position, width):
        yield from vertical_moves(state, current_position, height)
        if at_major_diagonal_corner(current_position, height, width):
            yield from horizontal_moves(state, current_position, width)
            yield from major_axis_moves(state, current_position, height, width)
        elif at_minor_diagonal_corner(current_position, height, width):
            yield from horizontal_moves(state, current_position, width)
            yield from minor_axis_moves(state, current_position, height, width)
        else:
            if current_position.x == 0:
                yield move_right(state, current_position, width)
            else:
                yield move_left(state, current_position, width)
    elif at_horizontal_edge(current_position, height):
        yield from horizontal_moves(state, current_position, width)
        if at_major_diagonal_corner(current_position, height, width):
            yield from vertical_moves(state, current_position, height)
            yield from major_axis_moves(state, current_position, height, width)
        elif at_minor_diagonal_corner(current_position, height, width):
            yield from vertical_moves(state, current_position, height)
            yield from minor_axis_moves(state, current_position, height, width)
        else:
            if current_position.y == 0:
                yield move_down(state, current_position, height)
            else:
                yield move_up(state, current_position, height)
    else:
        yield from vertical_moves(state, current_position, height)
        yield from horizontal_moves(state, current_position, height)


def vertical_moves(state, current_position, height):
    if height <= 2:
        if current_position.y == 0:
            yield move_down(state, current_position, height)
        if current_position.y == height - 1:
            yield move_up(state, current_position, height)
    else:
        yield move_down(state, current_position, height)
        yield move_up(state, current_position, height)


def horizontal_moves(state, current_position, width):
    yield move_left(state, current_position, width)
    yield move_right(state, current_position, width)


def major_axis_moves(state, current_position, height, width):
    yield move_up_left(state, current_position, height, width)
    yield move_down_right(state, current_position, height, width)


def minor_axis_moves(state, current_position, height, width):
    yield move_up_right(state, current_position, height, width)
    yield move_down_left(state, current_position, height, width)


def move_up(state, current_position, height):
    cost = 2 if current_position.y == 0 else 1
    new_y = decrement_axis(current_position.y, height)
    new_state = get_new_sate(state, current_position.x, current_position.y, current_position.x, new_y)
    new_position = Position(current_position.x, new_y)
    return new_state, new_position, cost


def move_down(state, current_position, height):
    cost = 2 if current_position.y == height - 1 else 1
    new_y = increment_axis(current_position.y, height)
    new_state = get_new_sate(state, current_position.x, current_position.y, current_position.x, new_y)
    new_position = Position(current_position.x, new_y)
    return new_state, new_position, cost


def move_left(state, current_position, width):
    cost = 2 if current_position.x == 0 else 1
    new_x = decrement_axis(current_position.x, width)
    new_state = get_new_sate(state, current_position.x, current_position.y, new_x, current_position.y)
    new_position = Position(new_x, current_position.y)
    return new_state, new_position, cost


def move_right(state, current_position, width):
    cost = 2 if current_position.x == width - 1 else 1
    new_x = increment_axis(current_position.x, width)
    new_state = get_new_sate(state, current_position.x, current_position.y, new_x, current_position.y)
    new_position = Position(new_x, current_position.y)
    return new_state, new_position, cost


def move_up_right(state, current_position, height, width):
    new_x = increment_axis(current_position.x, width)
    new_y = decrement_axis(current_position.y, height)
    new_state = get_new_sate(state, current_position.x, current_position.y, new_x, new_y)
    new_position = Position(new_x, new_y)
    return new_state, new_position, 3


def move_up_left(state, current_position, height, width):
    new_x = decrement_axis(current_position.x, width)
    new_y = decrement_axis(current_position.y, height)
    new_state = get_new_sate(state, current_position.x, current_position.y, new_x, new_y)
    new_position = Position(new_x, new_y)
    return new_state, new_position, 3


def move_down_left(state, current_position, height, width):
    new_x = decrement_axis(current_position.x, width)
    new_y = increment_axis(current_position.y, height)
    new_state = get_new_sate(state, current_position.x, current_position.y, new_x, new_y)
    new_position = Position(new_x, new_y)
    return new_state, new_position, 3


def move_down_right(state, current_position, height, width):
    new_x = increment_axis(current_position.x, width)
    new_y = increment_axis(current_position.y, height)
    new_state = get_new_sate(state, current_position.x, current_position.y, new_x, new_y)
    new_position = Position(new_x, new_y)
    return new_state, new_position, 3


def get_new_sate(state, current_x, current_y, new_x, new_y):
    new_state = copy.deepcopy(state)
    new_state[current_y][current_x], new_state[new_y][new_x] = new_state[new_y][new_x], new_state[current_y][current_x]
    return new_state


def increment_axis(index, length):
    return (index + 1) % length


def decrement_axis(index, length):
    return (index - 1) % length


def at_corner(current_position, height, width):
    return at_minor_diagonal_corner(current_position, height, width) or at_major_diagonal_corner(current_position,
                                                                                                 height, width)


def at_major_diagonal_corner(current_position, height, width):
    return ((current_position.x == 0 and current_position.y == 0)
            or (current_position.x == width - 1 and current_position.y == height - 1)
            )


def at_minor_diagonal_corner(current_position, height, width):
    return ((current_position.x == width - 1 and current_position.y == 0)
            or (current_position.x == 0 and current_position.y == height - 1)
            )


def at_vertical_edge(current_position, width):
    return current_position.x == 0 or current_position.x == width - 1


def at_horizontal_edge(current_position, height):
    return current_position.y == 0 or current_position.y == height - 1

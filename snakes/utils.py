import direction
import math


def get_next_coord(curr_coord, a_dir):
    next_coord = curr_coord.copy()
    if a_dir == direction.RIGHT:
        next_coord['x'] += 1
    elif a_dir == direction.LEFT:
        next_coord['x'] -= 1
    elif a_dir == direction.UP:
        next_coord['y'] -= 1
    elif a_dir == direction.DOWN:
        next_coord['y'] += 1

    return next_coord


def is_coord_on_board(coord, board) -> bool:
    return 0 <= coord['x'] < board['width'] and \
           0 <= coord['y'] < board['height']


def get_dist(coord1, coord2) -> int:
    return abs(coord2['x'] - coord1['x']) + abs(coord2['y'] - coord1['y'])


def get_directions(from_coord, to_coord):
    dx = to_coord['x'] - from_coord['x']
    dy = to_coord['y'] - from_coord['y']
    sign = lambda x: (1, 0)[x < 0]
    h_dir = (direction.LEFT, direction.RIGHT)[sign(dx)]
    v_dir = (direction.UP, direction.DOWN)[sign(dy)]

    if abs(dx) > abs(dy):
        return h_dir, v_dir

    return v_dir, h_dir


def get_opposite_direction(a_dir):
    if a_dir == direction.LEFT:
        return direction.RIGHT
    elif a_dir == direction.RIGHT:
        return direction.LEFT
    elif a_dir == direction.UP:
        return direction.DOWN
    else:
        return direction.UP

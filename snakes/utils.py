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


def get_direction(from_coord, to_coord):
    vec = (to_coord['x'] - from_coord['x'], to_coord['y'] - from_coord['y'])
    angle = math.atan2(vec[1], vec[0])
    if (math.pi / 4) <= angle < (math.pi * 3 / 4):
        return direction.DOWN
    elif (math.pi * 3 / 4) <= angle < (math.pi * 5 / 4):
        return direction.LEFT
    elif (math.pi * 5 / 4) <= angle < (math.pi * 7 / 4):
        return direction.UP
    else:
        return direction.RIGHT


def get_opposite_direction(a_dir):
    if a_dir == direction.LEFT:
        return direction.RIGHT
    elif a_dir == direction.RIGHT:
        return direction.LEFT
    elif a_dir == direction.UP:
        return direction.DOWN
    else:
        return direction.UP

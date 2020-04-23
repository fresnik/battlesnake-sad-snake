import direction


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

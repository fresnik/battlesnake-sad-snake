from direction import all_directions, DEFAULT_DIRECTION
from gamestate import GameState
from snakes.basesnake import BaseSnake
from snakes.utils import get_next_coord, is_coord_on_board


class ClaustrophobicSnake(BaseSnake):
    """Goes in the direction that leads to a larger area"""
    def get_next_move(self, game_state: GameState) -> str:
        body = game_state.data['you']['body']
        head = body[0]
        largest_area = 0
        largest_area_direction = DEFAULT_DIRECTION

        for a_dir in all_directions:
            next_head_coord = get_next_coord(head, a_dir)

            size = game_state.get_size_of_empty_cells(next_head_coord)
            print(f'The area is of size {size} if I go {a_dir}...')

            if size > largest_area:
                largest_area_direction = a_dir
                largest_area = size

        return largest_area_direction

from direction import all_directions, DEFAULT_DIRECTION
from gamestate import GameState
from snakes.basesnake import BaseSnake
from snakes.utils import get_next_coord, is_coord_on_board


class AvoidWallsAndSelfSnake(BaseSnake):
    def get_next_move(self, game_state: GameState) -> str:
        body = game_state.data['you']['body']
        head = body[0]

        for a_dir in all_directions:
            next_head_coord = get_next_coord(head, a_dir)
            if is_coord_on_board(next_head_coord, game_state.data['board']) and \
                    next_head_coord not in body:
                return a_dir

        return DEFAULT_DIRECTION

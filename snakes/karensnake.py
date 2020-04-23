from direction import RIGHT
from gamestate import GameState
from snakes.basesnake import BaseSnake


class KarenSnake(BaseSnake):
    """KarenSnake will always go right, because Karen is always right"""
    def get_next_move(self, game_state: GameState) -> str:
        return RIGHT

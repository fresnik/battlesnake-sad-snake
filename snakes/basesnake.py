from gamestate import GameState


class BaseSnake:
    def __init__(self):
        pass

    def get_next_move(self, game_state: GameState) -> str:
        raise NotImplementedError('Subclasses should implement this!')

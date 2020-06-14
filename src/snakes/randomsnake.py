import snakes.basesnake
import direction
import random

from gamestate import GameState


class RandomSnake(snakes.basesnake.BaseSnake):
    def get_next_move(self, _: GameState) -> str:
        return random.choice(direction.all_directions)

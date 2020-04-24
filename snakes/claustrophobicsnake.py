from direction import all_directions, DEFAULT_DIRECTION
from gamestate import GameState
from snakes.basesnake import BaseSnake
from snakes.utils import get_next_coord, get_dist, get_direction, get_opposite_direction

import random


class ClaustrophobicSnake(BaseSnake):
    """Goes in the direction that leads to a larger area"""
    def get_next_move(self, game_state: GameState) -> str:
        body = game_state.data['you']['body']
        head = body[0]

        # TODO: If we're starving - aim for nearby food

        # If our head is close to the head of another longer snake, try to steer away if possible
        for snake in game_state.data['board']['snakes']:
            if snake['id'] == game_state.data['you']['id']:
                continue

            if len(snake['body']) <= len(game_state.data['you']['body']):
                continue

            d = get_dist(head, snake['body'][0])
            if d <= 4:
                e_direction = get_direction(head, snake['body'][0])
                e_direction = get_opposite_direction(e_direction)
                print(f'snake {snake["name"]} is too close and big, trying opposite direction, to the {e_direction}...')

                next_head_coord = get_next_coord(head, e_direction)
                if next_head_coord not in game_state.snake_body_cells:
                    return e_direction

        # Move in the direction of the largest area
        largest_area = 0
        largest_area_directions = []

        for a_dir in all_directions:
            next_head_coord = get_next_coord(head, a_dir)

            size = game_state.get_size_of_empty_cells(next_head_coord)
            print(f'The area is of size {size} if I go {a_dir}...')

            if size == largest_area:
                largest_area_directions.append(a_dir)
            elif size > largest_area:
                largest_area_directions = [a_dir]
                largest_area = size

        if len(largest_area_directions) == 0:
            return DEFAULT_DIRECTION

        return random.choice(largest_area_directions)

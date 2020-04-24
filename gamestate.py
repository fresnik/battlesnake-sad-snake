class GameState:
    def __init__(self, data):
        self.data = data
        self.snake_body_cells = []
        for snake in self.data['board']['snakes']:
            self.snake_body_cells += snake['body']

    def get_board(self):
        return self.data["board"]

    def is_coord_on_board(self, coord) -> bool:
        return 0 <= coord['x'] < self.data['board']['width'] and \
               0 <= coord['y'] < self.data['board']['height']

    def get_empty_cells_around_coord(self, coord) -> list:
        # List of all cells connected orthogonally to coord
        coords = [{'x': coord['x'] + 1, 'y': coord['y']},
                  {'x': coord['x'] - 1, 'y': coord['y']},
                  {'x': coord['x'], 'y': coord['y'] - 1},
                  {'x': coord['x'], 'y': coord['y'] + 1}]

        # Filter coords list based on that coord not being taken by the body of a snake and it being on the board
        empty_coords = [c for c in coords if c not in self.snake_body_cells and self.is_coord_on_board(c)]

        return empty_coords

    def get_size_of_empty_cells(self, start_coord) -> int:
        if start_coord in self.snake_body_cells:
            return 0

        visited = []  # List to keep track of visited nodes.
        queue = []  # Initialize a queue

        def bfs(node):
            visited.append(node)
            queue.append(node)

            while queue:
                s = queue.pop(0)
                # print(s, end=" ")

                neighbours = self.get_empty_cells_around_coord(s)
                for neighbour in neighbours:
                    if neighbour not in visited:
                        visited.append(neighbour)
                        queue.append(neighbour)

        bfs(start_coord)

        return len(visited)

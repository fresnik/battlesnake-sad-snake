class GameState:
    def __init__(self, data):
        self.data = data

    def get_board_width(self):
        return self.data["board"]["width"]

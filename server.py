import os
import random

import cherrypy

from snakes.avoidwallssnake import AvoidWallsSnake
from gamestate import GameState

"""
This is a simple Battlesnake server written in Python.
For instructions see https://github.com/BattlesnakeOfficial/starter-snake-python/README.md
"""


class Battlesnake(object):
    @cherrypy.expose
    def index(self):
        return '<div style="font-size:100pt;text-align:center;">🐍</div>'

    @cherrypy.expose
    def ping(self):
        return "pong"

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def start(self):
        data = cherrypy.request.json
        print("START")
        return {"color": "#DEADC0DE", "headType": "dead", "tailType": "block-bum"}

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def move(self):
        data = cherrypy.request.json

        snake = AvoidWallsSnake()
        game_state = GameState(data)

        move = snake.get_next_move(game_state)

        print(f"MOVE: {move}")
        return {"move": move}

    @cherrypy.expose
    @cherrypy.tools.json_in()
    def end(self):
        data = cherrypy.request.json
        print("END")
        return "ok"


if __name__ == "__main__":
    server = Battlesnake()
    cherrypy.config.update({"server.socket_host": "0.0.0.0"})
    cherrypy.config.update(
        {"server.socket_port": int(os.environ.get("PORT", "8000")),}
    )
    print("Starting Battlesnake Server...")
    cherrypy.quickstart(server)

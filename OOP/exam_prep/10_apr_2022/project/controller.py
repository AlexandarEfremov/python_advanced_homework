from typing import List

from project.player import Player
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def add_player(self, *args: Player):
        add_list = []
        for item in args:
            player = next((p for p in self.players if p.name == item.name), None)
            if player:
                continue
            self.players.append(item)
            add_list.append(item.name)
        return f"Successfully added: {', '.join(add_list)}"

    def add_supply(self, *args: Supply):
        for supp in args:
            self.supplies.append(supp)

    def sustain(self, player_name: str, sustenance_type: str):
        pass

    def duel(self, first_player_name: str, second_player_name: str):
        pass

    def next_day(self):
        pass

    def __str__(self):
        pass

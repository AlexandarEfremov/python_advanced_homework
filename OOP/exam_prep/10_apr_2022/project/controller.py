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
        if sustenance_type == "Food" or sustenance_type == "Drink":
            player = next((p for p in self.players if p.name == player_name), None)
            if player:
                if player.stamina == 100:
                    return f"{player_name} have enough stamina."
                if sustenance_type == "Food":
                    food_available = next((f for f in reversed(self.supplies) if f.__class__.__name__ == "Food"), None)
                    if food_available is None:
                        raise Exception("There are no food supplies left!")
                    else:
                        player.stamina += food_available.energy
                        self.supplies.remove(food_available)
                        if player.stamina > 100:
                            player.stamina = 100
                elif sustenance_type == "Drink":
                    drink_available = next((d for d in reversed(self.supplies) if d.__class__.__name__ == "Drink"), None)
                    if drink_available is None:
                        raise Exception("There are no drink supplies left!")



    def duel(self, first_player_name: str, second_player_name: str):
        pass

    def next_day(self):
        pass

    def __str__(self):
        pass

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
            if player is None:
                self.players.append(item)
                add_list.append(item.name)
            else:
                continue
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
                        if player.stamina + food_available.energy < 100:
                            player.stamina += food_available.energy
                            self.supplies.remove(food_available)
                        else:
                            player.stamina = 100
                        return f"{player_name} sustained successfully with {food_available.name}."
                elif sustenance_type == "Drink":
                    drink_available = next((d for d in reversed(self.supplies) if d.__class__.__name__ == "Drink"), None)
                    if drink_available is None:
                        raise Exception("There are no drink supplies left!")
                    else:
                        if player.stamina + drink_available.energy < 100:
                            player.stamina += drink_available.energy
                            self.supplies.remove(drink_available)
                        else:
                            player.stamina = 100
                        return f"{player_name} sustained successfully with {drink_available.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player_one = next((p for p in self.players if p.name == first_player_name), None)
        player_two = next((p for p in self.players if p.name == second_player_name), None)
        if player_one.stamina <= 0 and player_two.stamina <= 0:
            res = [f"Player {first_player_name} does not have enough stamina.",
                   f"Player {second_player_name} does not have enough stamina."]
            return "\n".join(res)

        if player_one.stamina <= 0:
            return f"Player {first_player_name} does not have enough stamina."
        if player_two.stamina <= 0:
            return f"Player {second_player_name} does not have enough stamina."

        if player_one.stamina < player_two.stamina:
            winner = None
            player_two.stamina -= 0.5 * player_one.stamina
            if player_two.stamina <= 0:
                player_two.stamina = 0
                winner = player_one.name
            else:
                player_one.stamina -= 0.5 * player_two.stamina
                if player_one.stamina <= 0:
                    player_one.stamina = 0
                    winner = player_two.name
                else:
                    winner = player_one.name if player_one.stamina > player_two.stamina else player_two.name
            return f"Winner: {winner}"

        else:
            winner = None
            player_one.stamina -= 0.5 * player_two.stamina
            if player_one.stamina <= 0:
                player_one.stamina = 0
                winner = player_two.name
            else:
                player_two.stamina -= 0.5 * player_one.stamina
                if player_two.stamina <= 0:
                    player_two.stamina = 0
                    winner = player_one.name
                else:
                    winner = player_one.name if player_one.stamina > player_two.stamina else player_two.name
            return f"Winner: {winner}"

    def next_day(self):
        for p in self.players:
            if p.stamina - (p.age * 2) > 0:
                p.stamina -= p.age * 2
            else:
                p.stamina = 0
            self.sustain(p.name, "Food")
            self.sustain(p.name, "Drink")

    def __str__(self):
        result = []
        [result.append(p.__str__()) for p in self.players]
        [result.append(s.details()) for s in self.supplies]
        return "\n".join(result)

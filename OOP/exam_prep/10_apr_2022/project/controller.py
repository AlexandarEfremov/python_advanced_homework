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
        self.supplies.extend(args)

    def __take_last_supply(self, supply_type: str):
        for i in range(len(self.supplies) - 1, 0, -1):
            if type(self.supplies[i]).__name__ == supply_type:
                return self.supplies.pop(i)
        if supply_type == "Food":
            raise Exception("There are no food supplies left!")
        if supply_type == "Drink":
            raise Exception("There are no drink supplies left!")

    def sustain(self, player_name: str, sustenance_type: str):
        if sustenance_type == "Food" or sustenance_type == "Drink":
            player = next((p for p in self.players if p.name == player_name), None)
            if player:
                if player.stamina == 100:
                    return f"{player_name} have enough stamina."
                supply = self.__take_last_supply(sustenance_type)
                if supply:
                    if player.stamina + supply.energy < 100:
                        player.stamina += supply.energy
                        return f"{player_name} sustained successfully with {supply.name}."
                    else:
                        player.stamina = 100
                        return f"{player_name} sustained successfully with {supply.name}."

    @staticmethod
    def __check_if_players_can_duel(*players):
        result = []
        for p in players:
            if p.stamina <= 0:
                result.append(f"Player {p.name} does not have enough stamina.")
        if result:
            return "\n".join(result)

    def duel(self, first_player_name: str, second_player_name: str):
        player_one = next((p for p in self.players if p.name == first_player_name), None)
        player_two = next((p for p in self.players if p.name == second_player_name), None)

        result = self.__check_if_players_can_duel(player_one, player_two)
        if result:
            return result

        if player_one.stamina < player_two.stamina:
            player_two.stamina -= 0.5 * player_one.stamina
            if player_two.stamina <= 0:
                player_two.stamina = 0
                return f"Winner: {player_one.name}"
            else:
                player_one.stamina -= 0.5 * player_two.stamina
                if player_one.stamina <= 0:
                    player_one.stamina = 0
                    return f"Winner: {player_two.name}"
                else:
                    return f"Winner: {player_one.name if player_one.stamina > player_two.stamina else player_two.name}"
        else:
            player_one.stamina -= 0.5 * player_two.stamina
            if player_one.stamina <= 0:
                player_one.stamina = 0
                return f"Winner: {player_two.name}"
            else:
                player_two.stamina -= 0.5 * player_one.stamina
                if player_two.stamina <= 0:
                    player_two.stamina = 0
                    return f"Winner: {player_one.name}"
                else:
                    return f"Winner: {player_one.name if player_one.stamina > player_two.stamina else player_two.name}"

    def next_day(self):
        for p in self.players:
            if p.stamina - (p.age * 2) > 0:
                p.stamina -= (p.age * 2)
            else:
                p.stamina = 0
            self.sustain(p.name, "Food")
            self.sustain(p.name, "Drink")

    def __str__(self):
        result = []
        [result.append(p.__str__()) for p in self.players]
        [result.append(s.details()) for s in self.supplies]
        return "\n".join(result)
from project1.player import Player


class Guild:
    def __init__(self):
        self.players = []

    def assign_player(self, player):
        self.players.append(player)
        return f"Welcome player {Player.player_info(player)} to the guild {Player.guild}"
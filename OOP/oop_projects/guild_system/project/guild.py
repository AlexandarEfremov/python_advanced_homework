from project.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        if player.guild != self.name and player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        self.players.append(player)
        player.guild = self.name

        if player.name not in self.skills_dict:
            self.skills_dict[player.name] = {}

        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        if player_name not in self.players:
            return f"Player {player_name} is not in the guild."
        self.players.remove(player_name)
        player_name.guild = "Unaffiliated"

    def guild_info(self):
        players_in_guild = "\n".join(player.player_info() for player in self.players)
        return f"Guild: {self.name}\n" \
               f"{players_in_guild}"


player = Player("George", 50, 100)

print(player.add_skill("Shield Break", 20))

print(player.player_info())

guild = Guild("UGT")

print(guild.assign_player(player))

print(guild.guild_info())
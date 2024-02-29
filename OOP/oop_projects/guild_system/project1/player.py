class Player:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills_dict = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name not in self.skills_dict:
            self.skills_dict[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        return "Skill already added"

    def player_info(self):
        return f"Name: {self.name}\nGuild: {self.guild}\n HP: {self.hp}\nMP: {self.mp}\n \
                {'\n'.join(f'{k}:{v}' for k, v in self.skills_dict.items())}"

class Player:
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills_dict = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if self.name not in self.skills_dict:
            self.skills_dict[self.name] = {}
        if skill_name not in self.skills_dict[self.name]:
            self.skills_dict[self.name][skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        return "Skill already added"

    def player_info(self):
        if self.name in self.skills_dict:
            player_details = f"\n".join(f'==={k} - {v}' for k, v in self.skills_dict[self.name].items())
            return f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n" \
                   f"{player_details}"
        return f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n"

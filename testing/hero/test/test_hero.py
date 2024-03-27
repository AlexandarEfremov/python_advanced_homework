from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("Alex", 5, 200, 100)
        self.enemy = Hero("Enemy", 4, 100, 50)

    def test_correct_init(self):
        self.assertEqual("Alex", self.hero.username)
        self.assertEqual(5, self.hero.level)
        self.assertEqual(200, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_enemy_correct_init(self):
        self.assertEqual("Enemy", self.enemy.username)
        self.assertEqual(4, self.enemy.level)
        self.assertEqual(100, self.enemy.health)
        self.assertEqual(50, self.enemy.damage)

    def test_battle_exception_if_fighting_self(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_when_not_enough_health(self):
        self.hero.health = 0
        expected_string = "Your health is lower than or equal to 0. You need to rest"

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual(expected_string, str(ve.exception))

    def test_battle_with_unrested_enemy(self):
        self.enemy.health = 0
        expected_string = f"You cannot fight {self.enemy.username}. He needs to rest"

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual(expected_string, str(ve.exception))

    def test_hero_health_after_damage(self):
        expected_health = self.hero.health - (self.enemy.damage * self.enemy.level)
        self.hero.battle(self.enemy)

        self.assertEqual(expected_health, self.hero.health)

    def test_enemy_health_after_damage(self):
        expected_health = self.enemy.health - (self.hero.damage * self.hero.level)
        self.enemy.battle(self.hero)

        self.assertEqual(expected_health, self.enemy.health)

    def test_draw_scenario(self):
        self.hero.health = 1
        self.enemy.health = 1

        self.assertEqual("Draw",self.hero.battle(self.enemy))

    def test_hero_wins_battle(self):
        self.hero.health = 10000
        self.assertEqual("You win", self.hero.battle(self.enemy))

    def test_hero_attributes_after_victory(self):
        self.hero.health = 10000
        self.hero.battle(self.enemy)

        self.assertEqual(6, self.hero.level)
        self.assertEqual(9805, self.hero.health)
        self.assertEqual(105, self.hero.damage)

    def test_enemy_wins_battle(self):
        self.enemy.health = 10000
        self.assertEqual("You win", self.enemy.battle(self.hero))

    def test_enemy_attributes_after_victory(self):
        self.enemy.health = 10000
        self.enemy.battle(self.hero)

        self.assertEqual(5, self.enemy.level)
        self.assertEqual(9505, self.enemy.health)
        self.assertEqual(55, self.enemy.damage)

    def test_correct_string_return(self):
        expected_string = f"Hero Alex: 5 lvl\nHealth: 200\nDamage: 100\n"

        self.assertEqual(expected_string, self.hero.__str__())



if __name__ == "__main__":
    main()
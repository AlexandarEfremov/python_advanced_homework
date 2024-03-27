from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("Alex", 1, 100, 100)
        self.enemy = Hero("Enemy", 1, 50, 50)

    def test_correct_init(self):
        self.assertEqual("Alex", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_enemy_correct_init(self):
        self.assertEqual("Enemy", self.enemy.username)
        self.assertEqual(1, self.enemy.level)
        self.assertEqual(50, self.enemy.health)
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

    def test_battle_returns_draw_and_decreases_health_for_both(self):
        self.hero.health = 50

        result = self.hero.battle(self.enemy)

        self.assertEqual("Draw", result)
        self.assertEqual(-50, self.enemy.health)
        self.assertEqual(0, self.hero.health)

    def test_fight_enemy_and_win(self):
        expected_level = self.hero.level + 1
        expected_health = self.hero.health - self.enemy.damage + 5
        expected_damage = self.hero.damage + 5

        result = self.hero.battle(self.enemy)

        self.assertEqual("You win", result)
        self.assertEqual(expected_level, self.hero.level)
        self.assertEqual(expected_health, self.hero.health)
        self.assertEqual(expected_damage, self.hero.damage)

    def test_fight_enemy_and_lose(self):
        self.enemy.health = 200
        expected_level = self.enemy.level + 1
        expected_health = self.enemy.health - self.hero.damage + 5
        expected_damage = self.enemy.damage + 5

        result = self.hero.battle(self.enemy)

        self.assertEqual("You lose", result)
        self.assertEqual(expected_level, self.enemy.level)
        self.assertEqual(expected_health, self.enemy.health)
        self.assertEqual(expected_damage, self.enemy.damage)

    def test_correct_string_return(self):
        expected_string = f"Hero Alex: 1 lvl\nHealth: 100\nDamage: 100\n"

        self.assertEqual(expected_string, self.hero.__str__())



if __name__ == "__main__":
    main()
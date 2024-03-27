from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Misha", "cat", "meow")

    def test_init(self):
        self.assertEqual("Misha", self.mammal.name)
        self.assertEqual("cat", self.mammal.type)
        self.assertEqual("meow", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_return_correct_sound(self):
        self.assertEqual("Misha makes meow", self.mammal.make_sound())

    def test_return_correct_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_return_correct_info(self):
        self.assertEqual("Misha is of type cat", self.mammal.info())


if __name__ == "__main__":
    main()
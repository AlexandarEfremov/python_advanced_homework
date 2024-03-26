from unittest import TestCase, main
from testing.projects.worker import Worker


class TestWorker(TestCase):
    def setUp(self):
        self.worker = Worker(
            "TestAlex",
            10_000,
            100,
        )

    def test_correct_init(self):
        self.assertEqual("TestAlex", self.worker.name)
        self.assertEqual(10_000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_if_rest_is_added_after_call(self):
        expected_energy = self.worker.energy + 1

        self.worker.rest()

        self.assertEqual(expected_energy, self.worker.energy)

    def test_if_error_when_energy_is_below_zero(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))


if __name__ == "__main__":
    main()

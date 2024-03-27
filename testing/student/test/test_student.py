from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student("Alex")
        self.student_with_courses = Student("Ewcia", {"math": ["x + y = z"]})

    def test_correct_init(self):
        self.assertEqual("Alex", self.student.name)
        self.assertEqual("Ewcia", self.student_with_courses.name)

        self.assertEqual({}, self.student.courses)
        self.assertEqual({"math": ["x + y = z"]}, self.student_with_courses.courses)



if __name__ == "__main__":
    main()
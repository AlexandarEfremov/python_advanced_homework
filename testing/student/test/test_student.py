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

    def test_enroll_existing_course_note_added(self):
        result = self.student_with_courses.enroll("math", ["1 + 2 = 3"])

        self.assertEqual("Course already added. Notes have been updated.",
                         result)

        self.assertEqual(["x + y = z", "1 + 2 = 3"],
                         self.student_with_courses.courses["math"])

    def test_enroll_new_course_note_added(self):
        result = self.student.enroll("math", ["z + y = j"])

        self.assertEqual("Course and course notes have been added.", result)

        self.assertEqual(
            {"math": ["z + y = j"]}, self.student.courses
        )

if __name__ == "__main__":
    main()
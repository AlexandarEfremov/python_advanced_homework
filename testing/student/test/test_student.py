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

    def test_enroll_new_course_with_y_note_added(self):
        result = self.student.enroll(
            "math",
            ["x + y = z"],
            "Y"
        )

        self.assertEqual(
            "Course and course notes have been added.",
            result
        )

        self.assertEqual(
            {"math": ["x + y = z"]},
            self.student.courses
        )

    def test_enroll_new_course_with_no_note_added(self):
        result = self.student.enroll(
            "math",
            ["x + y = z"],
            "n"
        )

        self.assertEqual(
            "Course has been added.",
            result
        )

        self.assertEqual(
            {"math": []},
            self.student.courses
        )

    def test_add_notes_to_existing_course(self):
        result = self.student_with_courses.add_notes("math", "abcd")

        self.assertEqual("Notes have been updated", result)

    def test_add_notes_to_non_exist_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("POPO", "abcd")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))



if __name__ == "__main__":
    main()
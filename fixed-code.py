"""Student grading utility functions and unit tests.

This module provides utility functions to:
- Calculate the average score from a list of marks.
- Check whether a student has met the passing mark threshold.
- Determine the grade classification based on the student's average score.
"""

import unittest

# Grade boundary thresholds
MINIMUM_PASS_MARK = 40
DISTINCTION_THRESHOLD = 90
FIRST_CLASS_THRESHOLD = 60
SECOND_CLASS_THRESHOLD = 45


def calculate_average(marks_list: list[float]) -> float:
    """Calculate and return the arithmetic mean of a list of marks.

    Args:
        marks_list: A list of numerical marks/scores.

    Returns:
        float: The average mark. Returns 0.0 if the list is empty.
    """
    if not marks_list:
        return 0.0

    total_sum = 0
    for score in marks_list:
        total_sum += score

    return total_sum / len(marks_list)


def is_passing(student_mark: float) -> bool:
    """Determine if a student's score meets or exceeds the pass requirement.

    Args:
        student_mark: The score to evaluate.

    Returns:
        bool: True if the score is at or above the minimum pass mark (40),
              False otherwise.
    """
    return student_mark >= MINIMUM_PASS_MARK


def get_grade(average_score: float) -> str:
    """Classify the performance tier based on the student's average score.

    Evaluation hierarchy:
    - >= 90: "Distinction"
    - >= 60: "First"
    - >= 45: "Second"
    - < 45:  "Fail"

    Args:
        average_score: The calculated average mark.

    Returns:
        str: The grade classification label.
    """
    if average_score >= DISTINCTION_THRESHOLD:
        return "Distinction"
    elif average_score >= FIRST_CLASS_THRESHOLD:
        return "First"
    elif average_score >= SECOND_CLASS_THRESHOLD:
        return "Second"
    else:
        return "Fail"


# =====================================================================
# Unit Tests
# =====================================================================

class TestStudentUtils(unittest.TestCase):
    """Test suite verifying calculations, pass/fail checks, and grading rules."""

    def test_average_of_three_marks(self):
        scores = [80, 90, 100]
        self.assertEqual(calculate_average(scores), 90.0)

    def test_average_single_mark(self):
        scores = [40]
        self.assertEqual(calculate_average(scores), 40.0)

    def test_above_pass_mark(self):
        score_above_threshold = 41
        self.assertTrue(is_passing(score_above_threshold))

    def test_exact_pass_mark(self):
        exact_threshold_score = 40
        self.assertTrue(is_passing(exact_threshold_score))

    def test_below_pass_mark(self):
        failing_score = 39
        self.assertFalse(is_passing(failing_score))

    def test_distinction(self):
        distinction_score = 95
        self.assertEqual(get_grade(distinction_score), "Distinction")

    def test_first(self):
        first_class_score = 60
        self.assertEqual(get_grade(first_class_score), "First")

    def test_second(self):
        second_class_score = 45
        self.assertEqual(get_grade(second_class_score), "Second")

    def test_fail(self):
        failing_average = 30
        self.assertEqual(get_grade(failing_average), "Fail")


if __name__ == "__main__":
    unittest.main()

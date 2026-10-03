import unittest

from grader import score, letter, late_penalty


class GraderTests(unittest.TestCase):
    def test_score_sums_correct_points(self):
        sub = {
            "answers": [
                {"correct": True, "points": 2},
                {"correct": False, "points": 3},
                {"correct": True, "points": 5},
            ]
        }
        self.assertEqual(score(sub), 7)

    def test_letter_a(self):
        self.assertEqual(letter(9, 10), "A")

    def test_letter_f(self):
        self.assertEqual(letter(4, 10), "F")

    def test_late_penalty_one_day(self):
        self.assertAlmostEqual(late_penalty(1, 100), 90.0)


if __name__ == "__main__":
    unittest.main()

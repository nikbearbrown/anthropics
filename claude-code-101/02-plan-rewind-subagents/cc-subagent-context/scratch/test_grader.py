import unittest

from grader import score, letter


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


if __name__ == "__main__":
    unittest.main()

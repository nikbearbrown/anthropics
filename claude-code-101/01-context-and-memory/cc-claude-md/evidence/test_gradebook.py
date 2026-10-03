import io
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
import gradebook


class TestGradebook(unittest.TestCase):
    def test_average(self):
        with tempfile.TemporaryDirectory() as tmp:
            original_db = gradebook.DB
            gradebook.DB = Path(tmp) / "grades.json"
            try:
                gradebook.add("ada")
                gradebook.score("ada", 90)
                gradebook.score("ada", 80)
                buf = io.StringIO()
                with redirect_stdout(buf):
                    gradebook.report()
                self.assertIn("85.0", buf.getvalue())
            finally:
                gradebook.DB = original_db

    def test_remove(self):
        with tempfile.TemporaryDirectory() as tmp:
            original_db = gradebook.DB
            gradebook.DB = Path(tmp) / "grades.json"
            try:
                gradebook.add("ada")
                gradebook.score("ada", 90)
                gradebook.add("grace")
                buf = io.StringIO()
                with redirect_stdout(buf):
                    gradebook.remove("ada")
                self.assertIn("removed ada", buf.getvalue())
                self.assertEqual(gradebook.load(), {"grace": []})

                buf = io.StringIO()
                with redirect_stdout(buf):
                    gradebook.remove("nobody")
                self.assertIn("no such student", buf.getvalue())
            finally:
                gradebook.DB = original_db


if __name__ == "__main__":
    unittest.main()

"""test_auth.py — the definition of done for auth.py.

Contract:
- hash_password(password: str) -> str
- verify_password(password: str, stored: str) -> bool
"""
import hashlib, unittest, auth


class TestAuth(unittest.TestCase):
    def test_verify_roundtrip(self):
        stored = auth.hash_password("hunter2")
        self.assertTrue(auth.verify_password("hunter2", stored))

    def test_wrong_password_rejected(self):
        stored = auth.hash_password("hunter2")
        self.assertFalse(auth.verify_password("nope", stored))

    def test_empty_password_raises(self):
        with self.assertRaises(ValueError):
            auth.hash_password("")

    def test_not_plaintext(self):
        stored = auth.hash_password("hunter2")
        self.assertNotIn("hunter2", stored)

    def test_not_md5(self):
        stored = auth.hash_password("hunter2")
        md5 = hashlib.md5(b"hunter2").hexdigest()
        self.assertNotIn(md5, stored)


if __name__ == "__main__":
    unittest.main()

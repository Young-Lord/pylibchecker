import libchecker
import unittest


class Test(unittest.TestCase):
    def test_regex(self):
        self.assertTrue(libchecker.query("libjcore222.so"))

    def test_normal(self):
        self.assertTrue(libchecker.query("libxcrash.so"))


if __name__ == "__main__":
    unittest.main()

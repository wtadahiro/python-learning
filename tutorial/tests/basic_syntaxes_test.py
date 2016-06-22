import sys
import unittest

sys.path.append('../src')
from basic_syntaxes import BasicSyntaxes


class TestBasicSyntaxes(unittest.TestCase):
    def test_over10(self):
        obj = BasicSyntaxes()
        self.assertTrue(obj.over10(11))
        self.assertFalse(obj.over10(9))
        self.assertFalse(obj.over10(10))

    def test_fizzbuzz(self):
        target = BasicSyntaxes()
        self.assertEqual('fizzbuzz', target.fizzbuzz(30))
        self.assertEqual('fizz', target.fizzbuzz(6))
        self.assertEqual('buzz', target.fizzbuzz(10))
        self.assertEqual(None, target.fizzbuzz(8))

        with self.assertRaises(Exception):
            target.fizzbuzz(0)


if __name__ == '__main__':
    unittest.main()

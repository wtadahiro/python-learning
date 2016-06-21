import sys
sys.path.append('../src')
import unittest
from basic_syntaxes import BasicSyntaxes

class TestBasicSyntaxes(unittest.TestCase):

    def test_over10(self):
        obj = BasicSyntaxes()
        self.assertTrue(obj.over10(11))
        self.assertFalse(obj.over10(9))
        self.assertFalse(obj.over10(10))


if __name__ == '__main__':
    unittest.main()

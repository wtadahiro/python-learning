import unittest
import basic_syntaxes_test

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTest(loader.loadTestsFromModule(basic_syntaxes_test))

    unittest.TextTestRunner(verbosity=2).run(suite)

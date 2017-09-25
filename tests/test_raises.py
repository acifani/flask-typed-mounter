import unittest

from checker import TypedMounter

class RaisesTest(unittest.TestCase):
    def setUp(self):
        self.tm = TypedMounter()

    def test_null_app_error(self):
        with self.assertRaises(ValueError):
            @self.tm.attach_endpoint('/mul', methods=['GET', 'POST'])
            def multiplier(val1: int, val2: int = 5):
                return val1 * val2


if __name__ == '__main__':
    unittest.main()

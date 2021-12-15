import unittest
from multiples import Multiples


class MultipleTests(unittest.TestCase):
    def test_get_multiple_3(self):
        multiple = Multiples(3, 4)   
        self.assertEqual("RESIT", multiple.operation())

    def test_get_multiple_5(self):
        multiple = Multiples(5, 6)
        self.assertEqual("IT", multiple.operation())

    def test_get_multiple_3_and_5(self):
        multiple = Multiples(15, 16)
        self.assertEqual("INTEGRACIONES", multiple.operation())
 
    def test_get_multiple_2(self):
        multiple = Multiples(2, 3)
        self.assertEqual("2", multiple.operation())


if __name__ == '__main__':
    unittest.main()
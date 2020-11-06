import unittest
import conversor

class MyTestCase(unittest.TestCase):
    def test_something(self):
        conversor.numero_para_extenso(11.3)


if __name__ == '__main__':
    unittest.main()

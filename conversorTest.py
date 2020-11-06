import unittest
import conversor

class MyTestCase(unittest.TestCase):
    def test_something(self):
        print(conversor.numero_para_extenso("1321.05"))
        print(conversor.numero_para_extenso("0.05"))
        print(conversor.numero_para_extenso("113"))
        print(conversor.numero_para_extenso("13452345521.05"))


if __name__ == '__main__':
    unittest.main()

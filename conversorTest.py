import unittest
import conversor

class MyTestCase(unittest.TestCase):
    def test_something(self):
        print(conversor.numero_para_extenso("1321.05"))
        print(conversor.numero_para_extenso("0.05"))
        print(conversor.numero_para_extenso("113"))
        print(conversor.numero_para_extenso("113,12"))
        print(conversor.numero_para_extenso("asfsadf"))


if __name__ == '__main__':
    unittest.main()

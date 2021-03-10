import unittest
from app import Application
class Test(unittest.TestCase):
    def test_sum(self):
        obj = Application()
        assert obj.add(2,1) , 3
    def test_diff(self):
        obj = Application()
        assert obj.sub(2,1) , 1
    def test_mul(self):
        obj = Application()
        assert obj.mul(2,2) , 4

if __name__ == "__main__":
    unittest.main()
    print("Everything passed")

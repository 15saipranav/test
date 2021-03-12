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
        assert obj.mul(3,3) , 9
    def test_div(self):
        obj = Application()
        assert obj.div(3,3) , 1
if __name__ == "__main__":
    unittest.main()
    print("Everything passed")

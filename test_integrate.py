import unittest
from app import Application
class Test(unittest.TestCase):
    def test_all1(self):
        obj = Application()
        assert obj.add(obj.mul(2,3),obj.sub(obj.div(2,2),1)) , 7
    def test_all2(self):
        obj = Application()
        assert obj.div(obj.add(obj.mul(2,1),3),obj.sub(6,1)) , 1

if __name__ == "__main__":
    unittest.main()

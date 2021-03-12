import unittest
from app import Application
class Test(unittest.TestCase):
    def test_all(self):
        obj = Application()
        assert obj.add(obj.mul(2,3),obj.sub(obj.div(2,2),1)) , 7

if __name__ == "__main__":
    unittest.main()

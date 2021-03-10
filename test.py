import unittest
from app import Application
class Test(unittest.TestCase):
    def test_sum(self):
        obj = Application()
        assert obj.add(2,1) , 3
if __name__ == "__main__":
    unittest.main()
    print("Everything passed")

import unittest

class SimpleTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(1,1)

if __name__ =="__main__":
    unittest.main()
import unittest

class SubDate:
    def getTotalDayByYear(self , year) :
        if year==1 : 
            print(0)
            return 0
        else : 
            print(365)
            return 365

    def isLeapYear(self, year) :
       if year % 4 == 0: return True
       if year % 400 == 0: return True   
       if year % 100 == 0: return False
       return False


class SimpleTest(unittest.TestCase):
    def testGetDayByYear(self):
         subdate = SubDate()
         self.assertEqual(0,subdate.getTotalDayByYear(1))     
         self.assertEqual(365,subdate.getTotalDayByYear(2))

    def testLeapYear(self):
        subdate = SubDate()
        self.assertTrue(subdate.isLeapYear(0))
        self.assertFalse(subdate.isLeapYear(1))
        self.assertTrue(subdate.isLeapYear(4))
        self.assertFalse(subdate.isLeapYear(700))
        self.assertTrue(subdate.isLeapYear(1200))

if __name__ =="__main__":
    unittest.main()
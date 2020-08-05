import unittest
from student import student


s=student('mandeep',12,'cse')
class test_student(unittest.TestCase):

    

    def test_getName(self):
       
        self.assertEqual(s.get_name(),"mandeep")
    def test_getDetail(self):
       
        self.assertEqual(s.get_detail(),"name:mandeep| rollNo:12")
    
    def test_ispass(self):
        self.assertFalse(s.is_pass)

if __name__ == "__main__":
    unittest.main()
import unittest

class firstTest(unittest.TestCase):
    
    def test_upper(self):
        self.assertEqual('mandeep'.upper(), 'MANDEEP')
        self.assertEqual('kumar'.upper(), 'KUMAR')



if __name__=='__main__':

    unittest.main()
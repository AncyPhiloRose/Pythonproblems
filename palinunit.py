import unittest
import self
import palin
class check_palin(unittest.TestCase):
    def test_palin(self):
        str1 = 'abba'
        status = palin.check_palin (str1)
    self.assertEqual (status, True)
    def test_palin_failure(self):
       str1 = 'ab'
       status = palin.check_palin (str1)
    self.assertEqual (status, False)
if __name__ == '__main__':
    unittest.main ()
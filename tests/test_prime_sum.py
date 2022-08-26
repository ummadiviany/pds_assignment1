import unittest
from tasks.prime_sum import get_prime_sum

class TestPrimeSum(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(get_prime_sum(10), 17)
        
    def test_case_2(self):
        self.assertEqual(get_prime_sum(20), 77)
        
    
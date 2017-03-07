import unittest

from tdd import sub_solution

class Test_Solution(unittest.TestCase):
	"""docstring for Test_Solution"""

	def test_addition(self):
		self.assertTrue(sub_solution(10,20,"+"),30)
	
	def test_subtraction(self):
		self.assertTrue(sub_solution(20,10,"-"),10)
	
	def test_multiplication(self):
		self.assertNotEqual(sub_solution(10,20,"-"),200)
	
	def test_division(self):
		self.assertEqual(sub_solution(10,20,"/"),0.5)

	def test_modulo(self):
		self.assertTrue(sub_solution(10,20,"%"),0)

	

if __name__ == '__main__':
    unittest.main()
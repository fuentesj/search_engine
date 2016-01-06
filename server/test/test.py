import unittest

class QuickTest(unittest.TestCase):

	def test_call(self):
		self.assertEqual(1,1)


if __name__=="__main__":
	unittest.main()
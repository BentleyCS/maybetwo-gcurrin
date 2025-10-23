from unittest import TestCase
import TestAssignment

class Test(TestCase):
    def test_example(self):
        expected = 5
        actual = 5
        self.assertEqual(5,TestAssignment.example())

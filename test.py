import unittest

from sample import MyClass


class MyTest(unittest.TestCase):
    '''
    Simple testing class to provide example of usage for testing.
    '''
    def setUp(self):
        self.my_class_1 = MyClass(-1, 2)
        self.my_class_2 = MyClass(2, 2)

    def test_add(self):
        result_1 = self.my_class_1.add()
        result_2 = self.my_class_2.add()
        expected_1 = 1
        expected_2 = 4
        self.assertEqual(expected_1, result_1)
        self.assertEqual(expected_2, result_2)


    def test_add_positive_ok(self):
        result_1 = self.my_class_1.add_only_positive()
        result_2 = self.my_class_2.add_only_positive()
        expected_1 = None
        expected_2 = 4
        self.assertEqual(expected_1, result_1)
        self.assertEqual(expected_2, result_2)

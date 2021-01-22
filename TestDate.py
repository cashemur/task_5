import unittest
from date import Task_5


class TestTask_5(unittest.TestCase):
    def setUp(self):
        self.dateExist = Task_5(29, 2, 2000)
        self.dateNotExist = Task_5(29, 2, 1999)

    def test_date_exist(self):
        self.assertEqual(self.dateExist.IsExistDate(), True)
        self.assertEqual(self.dateNotExist.IsExistDate(), False)

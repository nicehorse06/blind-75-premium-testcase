# 253. Meeting Rooms II

def min_meeting_rooms(intervals):
    pass


import unittest
class TestMeetingRoomsII(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(min_meeting_rooms([[0,30],[5,10],[15,20]]), 2)

    def test_case_2(self):
        self.assertEqual(min_meeting_rooms([[7,10],[2,4]]), 1)

    def test_case_3(self):
        self.assertEqual(min_meeting_rooms([[1,5],[8,9],[8,9]]), 2)

    def test_case_4(self):
        self.assertEqual(min_meeting_rooms([[0, 30], [5, 10], [5, 15]]), 3)

    def test_case_5(self):
        self.assertEqual(min_meeting_rooms([[2, 4], [3, 5], [4, 6]]), 2)

    def test_case_6(self):
        self.assertEqual(min_meeting_rooms([[0, 5], [5, 10], [10, 15]]), 1)

    def test_case_7(self):
        self.assertEqual(min_meeting_rooms([[0, 5], [1, 2], [1, 10]]), 3)

    def test_case_8(self):
        self.assertEqual(min_meeting_rooms([[7, 10], [2, 4], [6, 8]]), 2)

    def test_case_9(self):
        self.assertEqual(min_meeting_rooms([[1, 10], [2, 6], [8, 10]]), 2)

    def test_case_10(self):
        self.assertEqual(min_meeting_rooms([[1, 3], [2, 4], [3, 5]]), 2)

if __name__ == '__main__':
    unittest.main()

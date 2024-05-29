# 252. Meeting Rooms 

def can_attend_meetings(intervals):
    pass


import unittest
class TestMeetingRooms(unittest.TestCase):
    def test_case_1(self):
        self.assertFalse(can_attend_meetings([[0,30],[5,10],[15,20]]))

    def test_case_2(self):
        self.assertTrue(can_attend_meetings([[7,10],[2,4]]))

    def test_case_3(self):
        self.assertFalse(can_attend_meetings([[1,5],[2,6],[8,10]]))

    def test_case_4(self):
        self.assertTrue(can_attend_meetings([[6,7],[8,9],[1,5]]))

    def test_case_5(self):
        self.assertTrue(can_attend_meetings([[1,2],[2,3],[3,4]]))

    def test_case_6(self):
        self.assertFalse(can_attend_meetings([[1,10],[2,6],[8,10]]))

    def test_case_7(self):
        self.assertTrue(can_attend_meetings([[5,8],[9,15]]))

    def test_case_8(self):
        self.assertFalse(can_attend_meetings([[1,3],[2,4],[3,5]]))

    def test_case_9(self):
        self.assertTrue(can_attend_meetings([[2,3],[3,4],[4,5]]))

    def test_case_10(self):
        self.assertFalse(can_attend_meetings([[1,5],[3,7],[8,10]]))

if __name__ == '__main__':
    unittest.main()

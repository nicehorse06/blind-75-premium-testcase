# 271. Encode and Decode Strings 加码解码字符串

class Codec:
    def encode(self, strs):
        pass
    
    def decode(self, s):
        pass


import unittest
class TestCodec(unittest.TestCase):
    def setUp(self):
        self.codec = Codec()

    def test_case_1(self):
        self.assertEqual(self.codec.decode(self.codec.encode(["hello", "world"])), ["hello", "world"])

    def test_case_2(self):
        self.assertEqual(self.codec.decode(self.codec.encode(["", ""])), ["", ""])

    def test_case_3(self):
        self.assertEqual(self.codec.decode(self.codec.encode(["a", "b", "c"])), ["a", "b", "c"])

    def test_case_4(self):
        self.assertEqual(self.codec.decode(self.codec.encode(["abc", "123", "xyz"])), ["abc", "123", "xyz"])

    def test_case_5(self):
        self.assertEqual(self.codec.decode(self.codec.encode(["", "abc"])), ["", "abc"])

    def test_case_6(self):
        self.assertEqual(self.codec.decode(self.codec.encode(["longstring", "anotherlongstring"])), ["longstring", "anotherlongstring"])

    def test_case_7(self):
        self.assertEqual(self.codec.decode(self.codec.encode(["a"*1000, "b"*1000])), ["a"*1000, "b"*1000])

    def test_case_8(self):
        self.assertEqual(self.codec.decode(self.codec.encode(["#", "##", "###"])), ["#", "##", "###"])

    def test_case_9(self):
        self.assertEqual(self.codec.decode(self.codec.encode(["a#b", "c#d"])), ["a#b", "c#d"])

    def test_case_10(self):
        self.assertEqual(self.codec.decode(self.codec.encode(["multiline\nstring", "another\nline"])), ["multiline\nstring", "another\nline"])

if __name__ == '__main__':
    unittest.main()

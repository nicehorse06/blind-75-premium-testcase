# 269. Alien Dictionary

def alienOrder(words):
    pass


import unittest
class TestAlienDictionary(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(alienOrder(["wrt", "wrf", "er", "ett", "rftt"]), "wertf")

    def test_example2(self):
        self.assertEqual(alienOrder(["z", "x"]), "zx")

    def test_example3(self):
        self.assertEqual(alienOrder(["z", "x", "z"]), "")

    def test_single_word(self):
        self.assertEqual(alienOrder(["z"]), "z")

    def test_single_letter(self):
        self.assertEqual(alienOrder(["z", "z", "z"]), "z")

    def test_no_valid_order(self):
        self.assertEqual(alienOrder(["abc", "ab"]), "")

    def test_complex_case(self):
        self.assertEqual(alienOrder(["za", "zb", "ca", "cb"]), "zacb")

    def test_identical_words(self):
        self.assertEqual(alienOrder(["aaa", "aaa", "aaa"]), "a")

    def test_empty_input(self):
        self.assertEqual(alienOrder([]), "")

    def test_longer_sequence(self):
        self.assertEqual(alienOrder(["abc", "abde", "abef"]), "abcfde")

if __name__ == "__main__":
    unittest.main()


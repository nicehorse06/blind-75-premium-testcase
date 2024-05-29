# 261. Graph Valid Tree

def validTree(n, edges):
    pass


import unittest
class TestGraphValidTree(unittest.TestCase):
    def test_example1(self):
        self.assertTrue(validTree(5, [[0,1], [0,2], [0,3], [1,4]]))

    def test_example2(self):
        self.assertFalse(validTree(5, [[0,1], [1,2], [2,3], [1,3], [1,4]]))

    def test_empty_graph(self):
        self.assertFalse(validTree(0, []))

    def test_single_node(self):
        self.assertTrue(validTree(1, []))

    def test_disconnected_graph(self):
        self.assertFalse(validTree(4, [[0,1], [2,3]]))

    def test_complete_tree(self):
        self.assertTrue(validTree(4, [[0,1], [1,2], [2,3]]))

    def test_cycle_in_small_graph(self):
        self.assertFalse(validTree(3, [[0,1], [1,2], [2,0]]))

    def test_valid_large_tree(self):
        self.assertTrue(validTree(6, [[0,1], [1,2], [1,3], [2,4], [2,5]]))

    def test_large_graph_with_cycle(self):
        self.assertFalse(validTree(6, [[0,1], [1,2], [1,3], [2,4], [2,5], [3,4]]))

    def test_two_clusters(self):
        self.assertFalse(validTree(5, [[0,1], [1,2], [3,4]]))

if __name__ == "__main__":
    unittest.main()

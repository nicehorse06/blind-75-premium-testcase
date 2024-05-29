# 323. Number of Connected Components in an Undirected Graph

def countComponents(n, edges):
    pass


import unittest
class TestNumberOfConnectedComponents(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(countComponents(5, [[0, 1], [1, 2], [3, 4]]), 2)

    def test_example2(self):
        self.assertEqual(countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]), 1)

    def test_no_edges(self):
        self.assertEqual(countComponents(5, []), 5)

    def test_single_node(self):
        self.assertEqual(countComponents(1, []), 1)

    def test_disconnected_nodes(self):
        self.assertEqual(countComponents(3, []), 3)

    def test_fully_connected_graph(self):
        self.assertEqual(countComponents(4, [[0, 1], [1, 2], [2, 3], [3, 0], [1, 3]]), 1)

    def test_linear_chain(self):
        self.assertEqual(countComponents(4, [[0, 1], [1, 2], [2, 3]]), 1)

    def test_complex_connection(self):
        self.assertEqual(countComponents(6, [[0, 1], [0, 2], [3, 4], [4, 5]]), 2)

    def test_clustered_graph(self):
        self.assertEqual(countComponents(10, [[0, 1], [1, 2], [2, 0], [3, 4], [5, 6], [7, 8], [8, 9]]), 4)

    def test_single_full_connection(self):
        self.assertEqual(countComponents(2, [[0, 1]]), 1)

if __name__ == "__main__":
    unittest.main()

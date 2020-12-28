import unittest
from unittest import TestCase
from DiGraph import DiGraph, NodeData
from src.GraphAlgo import GraphAlgo


def create_graph() -> DiGraph():
    graph = DiGraph()
    graph.add_node(0)
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_node(5)
    graph.add_node(6)
    graph.add_node(7)
    graph.add_node(8)
    graph.add_node(9)
    graph.add_node(10)
    graph.add_node(11)
    graph.add_node(12)
    graph.add_node(13)
    graph.add_node(14)
    graph.add_edge(1, 2, 0)
    graph.add_edge(2, 3, 4)
    graph.add_edge(3, 7, 9)
    graph.add_edge(7, 4, 7)
    graph.add_edge(4, 5, 5)
    graph.add_edge(5, 4, 6)
    graph.add_edge(5, 6, 2)
    graph.add_edge(6, 7, 15)
    graph.add_edge(7, 9, 2)
    graph.add_edge(9, 8, 1)
    graph.add_edge(8, 1, 3)
    graph.add_edge(10, 11, 7.5)
    graph.add_edge(10, 12, 0)
    graph.add_edge(11, 13, 0)
    graph.add_edge(12, 13, 0)
    graph.add_edge(9, 14, 3)
    #
    # Graph illustration:
    #
    #   (0)
    #                w=0
    #   (1)>------>-------->----->(2)
    #    ^           w=2           \>
    #    |      (5)>----->(6)        \
    #    |      ^   >        >        \
    #    ^      |    \        \        \
    #    |      |  w=6\    w=15\     w=4\
    #    |   w=5|      \        \        |
    # w=3|      |       \>       \>      >(3)
    #    |      ^-<-----<(4)<----<(7)<-----<
    #    |         w=5       w=7  \>   w=9
    #    ^                         \
    #    |                       w=2\
    #    |                           \>
    #    |--------<------<(8)<----<---(9)----->(14)
    #            w=3            w=1       w=3
    #
    #  	      w=7.5
    #  	(10)>-------->(11)
    #  	 >             |
    # w=0|             |w=0
    # 	 |             >
    # 	(12)>-------->(13)
    # 	       w=0
    #
    return graph


class TestGraphAlgo(unittest.TestCase):
    def test_shortest_path(self):
        graph = create_graph()
        graph_algo = GraphAlgo(graph)
        result = ""
        self.assertEqual(graph_algo.shortest_path(1, 7)[0], 13)
        self.assertEqual(graph_algo.shortest_path(1, 10)[0], -1)
        self.assertEqual(graph_algo.shortest_path(10, 13)[0], 0)
        self.assertEqual(graph_algo.shortest_path(7, 6)[0], 14)
        result = None
        directions = graph_algo.shortest_path(1, 7)[1]
        if directions is not None:
            result = ""
            for n in directions:
                result = result + str(n.key) + ", "
        # print(result)
        self.assertEqual(result, "1, 2, 3, 7, ")
        result = None
        directions = graph_algo.shortest_path(1, 10)[1]
        if directions is not None:
            result = ""
            for n in directions:
                result = result + str(n.key) + ", "
        # print(result)
        self.assertEqual(result, None)
        result = None
        directions = graph_algo.shortest_path(14, 9)[1]
        if directions is not None:
            result = ""
            for n in directions:
                result = result + str(n.key) + ", "
        # print(result)
        self.assertEqual(result, None)
        result = None
        directions = graph_algo.shortest_path(10, 13)[1]
        if directions is not None:
            result = ""
            for n in directions:
                result = result + str(n.key) + ", "
        # print(result)
        self.assertEqual(result, "10, 12, 13, ")
        result = None
        directions = graph_algo.shortest_path(7, 6)[1]
        if directions is not None:
            result = ""
            for n in directions:
                result = result + str(n.key) + ", "
        # print(result)
        self.assertEqual(result, "7, 4, 5, 6, ")


if __name__ == '__main__':
    unittest.main()

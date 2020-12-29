from typing import List
from queue import PriorityQueue
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
from DiGraph import DiGraph, NodeData


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, g: DiGraph = DiGraph()):
        self.DiGraph = g

    def get_graph(self) -> GraphInterface:
        return self.DiGraph

    def load_from_json(self, file_name: str) -> bool:
        pass

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if not self.DiGraph.graph.__contains__(id1) or not self.DiGraph.graph.__contains__(id2):
            return -1, None
        path_list = list()
        if id1 == id2:
            path_list.append(self.DiGraph.graph.get(id1))
            return 0, path_list
        path_len, path_dict = self.dijkstra(id1, id2, {})
        if path_dict is None:
            return -1, None
        src_node = self.DiGraph.graph.get(id1)
        dst_node = self.DiGraph.graph.get(id2)
        node_pointer = dst_node
        path_list.append(node_pointer)
        while True:
            node_pointer = path_dict.get(node_pointer)
            path_list.append(node_pointer)
            if node_pointer == src_node:
                break
        path_list.reverse()
        return path_len, path_list

    def connected_component(self, id1: int) -> list:
        pass

    def connected_components(self) -> List[list]:
        pass

    def plot_graph(self) -> None:
        pass

    def dijkstra(self, src, dst, the_path) -> (float, dict):
        pq = PriorityQueue()
        # node that we already check
        ch = {}  # key=int, val=node_data
        flag = False
        node_src = self.DiGraph.graph.get(src)
        node_src.tag = 1
        pq.put(node_src)
        ch.update({src: node_src})
        while not pq.empty() and not flag:
            n1 = pq.get()
            key1 = n1.key
            if key1 == dst:
                flag = True
            else:
                ed = self.DiGraph.all_out_edges_of_node(key1)
                for key2 in ed:
                    w = ed.get(key2)
                    n2 = self.DiGraph.graph.get(key2, NodeData())
                    w_key1 = n1.tag
                    if not ch.__contains__(key2) or ch.get(key2).tag > w_key1 + w:
                        if not ch.__contains__(key2):
                            n2.tag = 0
                        n2.tag = w_key1 + w
                        ch.update({key2: n2})
                        the_path.update({n2: n1})
                        pq.put(n2)
        if flag:
            return ch.get(dst).tag - 1, the_path
        return -1, None

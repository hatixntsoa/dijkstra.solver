import sys
from heapq import heapify, heappush

class Dijkstra:
    """
    Dijkstra's algorithm for finding the shortest path in a graph.
    
    Attributes:
        graph_to_solve (dict): The graph represented as a dictionary.
        inf (int): Represents infinity for the cost of nodes.
        visited_nodes (list): Keeps track of visited nodes during traversal.
    """
    def __init__(self, graph: dict = None) -> None:
        """
        Initializes the Dijkstra class with an optional graph.

        :param graph: A dictionary representing the graph. Defaults to None.
        """
        if graph:
          self.graph = graph

        self.inf = sys.maxsize
        self.visited_nodes = []

    @staticmethod
    def get_graph_size(graph: dict) -> int:
        """
        Returns the number of nodes in the graph.

        :param graph: The graph to evaluate.
        :return: Returns the size of the graph.
        """
        return len(graph)

    def get_node_data(self, graph: dict) -> dict:
        """
        Initializes node data with infinite costs and empty predecessors.

        :param graph: The graph for which to initialize node data.
        :return: Returns a dictionary containing each node's cost and predecessors.
        """
        node_data = {}

        for key in graph.keys():
            node_data[key] = {"cost": self.inf, "pred": []}

        return node_data

    @staticmethod
    def get_src_dest_node(graph: dict) -> list[str]:
        """
        Retrieves the list of keys (nodes) from the graph.

        :param graph: The graph to evaluate.
        :return: Returns a list of node keys from the graph.
        """
        list_of_keys = []

        for key in graph.keys():
            list_of_keys.append(key)

        return list_of_keys

    @staticmethod
    def get_default_nodes(source_node: str, destination_node: str, keys: list[str]) -> str:
        """
        Determines the default source and destination nodes.

        :param source_node: The desired source node.
        :param destination_node: The desired destination node.
        :param keys: The list of all nodes in the graph.
        :return: Returns a tuple containing the source and destination nodes.
        """
        if source_node is None:
            source_node = keys[0]  # get the first key

        if destination_node is None:
            destination_node = keys[-1]  # get the last key

        return source_node, destination_node

    def solve(self, graph: dict=None, source_node=None, destination_node=None) -> None:
        """
        Solves the shortest path problem using Dijkstra's algorithm.

        :param graph: The graph to analyze.
        :param source_node: The starting node. Defaults to None.
        :param destination_node: The target node. Defaults to None.
        """
        # Set the graph to solve to the passed graph or the class's graph
        if graph is not None:
          self.graph = graph

        node_data = self.get_node_data(self.graph)
        keys = self.get_src_dest_node(self.graph)

        source_node, destination_node = self.get_default_nodes(
            source_node, destination_node, keys
        )

        # Check if the source and destination nodes are valid
        is_solvable = True

        if source_node not in self.graph.keys():
            print(f"Sorry, {source_node} not in the graph")
            is_solvable = False

        if destination_node not in self.graph.keys():
            print(f"Sorry, {destination_node} not in the graph")
            is_solvable = False

        if is_solvable:
            graph_length = self.get_graph_size(node_data)
            node_data[source_node]["cost"] = 0
            current_node = source_node

            for _ in range(graph_length - 1):
                if current_node not in self.visited_nodes:
                    self.visited_nodes.append(current_node)
                    min_heap = []
                    for node in self.graph[current_node]:
                        if node not in self.visited_nodes:
                            cost = node_data[current_node]["cost"] + self.graph[current_node][node]
                            if cost < node_data[node]["cost"]:
                                node_data[node]["cost"] = cost
                                node_data[node]["pred"] = node_data[current_node]["pred"] + list(current_node)
                            heappush(min_heap, (node_data[node]["cost"], node))
                heapify(min_heap)
                current_node = min_heap[0][1]

            # Print the graph and the result
            print("Graph : \n")
            for key in self.graph.keys():
                print(f"{key} : {self.graph.get(key)}")
            print("")
            print(f"Path to go : {source_node} -> {destination_node}\n")
            print(f"""Shortest Distance : {node_data[destination_node]["cost"]}""")
            final_path = " -> ".join(node_data[destination_node]["pred"] + list(destination_node))
            print(f"Shortest Path     : {final_path}")
        else:
            print("Not solvable")

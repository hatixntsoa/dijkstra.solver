import string

class WeightedGraph:
  """A class to represent a weighted graph with nodes and neighbors."""

  def __init__(self) -> None:
    """
    Initialize an empty dictionary to store the graph structure.
    
    :param: None
    :return: None
    """
    self.graph: dict = {}

  def get(self) -> dict:
    """
    Return the current graph structure as a dictionary.
    
    :param: None
    :return: A dictionary representing the graph.
    """
    return self.graph
    
  def ask_neighbor(self) -> int:
    """
    Prompt the user to input the number of neighbors for a node.
    
    :param: None
    :return: An integer representing the number of neighbors.
    """
    return int(input("Enter the number of neighbors: "))
  
  def create(self, nodes: int) -> None:
    """
    Create the graph by adding nodes and their respective neighbors.

    For each node, the user is prompted to input its neighbors and the corresponding 
    edge weights. The nodes are labeled using uppercase letters (A, B, C, etc.).

    :param nodes: The number of nodes to be added to the graph.
    :return: None
    """
    for i in range(nodes):
      node = string.ascii_uppercase[i]
      print(f"\nNode N°{i+1}: {node}")
      neighbor_dict = {input(f"{node} Neighbor N°{j+1}: "): int(input(f"{node} Neighbor N°{j+1} weight: ")) 
                        for j in range(self.ask_neighbor())}
      print("")
      self.graph[node] = neighbor_dict

  def show(self) -> None:
    """
    Display the graph's nodes and their neighbors along with edge weights.

    Each node and its corresponding neighbors and weights are printed to the console.
    
    :param: None
    :return: None
    """
    for node, neighbors in self.graph.items():
      print(f"{node}: {neighbors}")

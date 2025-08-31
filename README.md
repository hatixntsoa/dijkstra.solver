# Dijkstra's Algorithm Solver

This Python implementation solves the shortest path problem in a weighted graph using **Dijkstra's algorithm**. It allows you to create a graph, specify source and destination nodes, and compute the shortest path between them.

## Features
- **Graph Representation**: The graph is represented as a dictionary, where each node has a list of neighbors and their respective weights.
- **Customizable Source and Destination**: If no source or destination is provided, the first and last nodes in the graph are chosen by default.
- **Heap-based Priority Queue**: The algorithm uses a heap (priority queue) for efficient node selection.
- **Shortest Path Calculation**: Returns both the shortest distance and the shortest path between two nodes.

## Installation

### From PyPI

To install the Dijkstra solver from PyPI, use the following command:

```bash
pip install dijkstra-solver
```

### From Source

1. Clone the repository:
   ```bash
   git clone https://github.com/hatixntsoa/dijkstra.solver.git
   ```

2. Navigate to the project directory:
   ```bash
   cd dijkstra.solver
   ```

3. Run the default code (just for testing):
   ```bash
   python dijkstra/main.py
   ```

4. Build the package:

  ```bash
  python setup.py sdist bdist_wheel
  ```

5. Install the package:

  ```bash
  pip install dist/dijkstra.solver-*.whl
  ```

## Usage

To use the Dijkstra solver, create a new python file, 
then here is the sample example:

1. Import the Dijkstra class and initialize the graph:
   ```python
   from dijkstra import Dijkstra
   
   # Define a weighted graph
   graph = {
       'A': {'B': 1, 'C': 4},
       'B': {'C': 2, 'D': 5},
       'C': {'D': 1},
       'D': {}
   }
   
   # Initialize the Dijkstra solver
   dijkstra = Dijkstra(graph)
   
   # Solve for the shortest path from A to D
   dijkstra.solve(source_node='A', destination_node='D')
   ```

2. The output will display the shortest distance and the path:
   ```
   Path: A -> D
   Shortest Distance: 4
   Shortest Path: A -> B -> C -> D
   ```

### Methods Overview

- **`get_graph_size(graph: dict)`**: Returns the number of nodes in the graph.
  
- **`get_node_data(graph: dict)`**: Initializes each node with an infinite cost and an empty predecessor.

- **`get_src_dest_node(graph: dict)`**: Returns a list of all nodes in the graph.

- **`get_default_nodes(source: str, destination: str, keys: list[str])`**: Sets default source and destination if none are provided.

- **`solve(graph: dict, source: str, destination: str)`**: Computes the shortest path from the source node to the destination node using Dijkstra's algorithm.

### Example Graph

Here is an example of a weighted graph:

```python
graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'C': 1, 'D': 4},
    'C': {'D': 2},
    'D': {}
}
```

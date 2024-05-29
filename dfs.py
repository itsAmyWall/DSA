# dfs_iterative.py

"""
Depth-First Search (DFS) Algorithm
==================================

Depth-First Search (DFS) is a fundamental algorithm used for traversing or searching 
through graph or tree data structures. It explores as far as possible along each branch 
before backtracking. Here is an overview of DFS, particularly focusing on the iterative 
implementation.

Characteristics:
----------------
1. Traversal Method: DFS explores as far as possible along each branch before backtracking.
2. Data Structure Used: Stack (explicitly managed in iterative DFS).
3. Path Finding: DFS does not guarantee the shortest path in an unweighted graph.

Time Complexity:
----------------
- O(V + E)
  - V: Number of vertices.
  - E: Number of edges.

Space Complexity:
-----------------
- O(V) for the stack and visited set.

Typical Use Cases:
------------------
1. Path Finding: Finding paths or checking for connectivity between nodes.
2. Cycle Detection: Detecting cycles in a graph.
3. Topological Sorting: Ordering nodes in a Directed Acyclic Graph (DAG).
4. Puzzle Solving: Solving puzzles with a single solution path (e.g., mazes).
5. Finding Strongly Connected Components: In directed graphs.

Iterative DFS Implementation in Python:
---------------------------------------
The following code demonstrates an iterative approach to performing DFS on a graph 
represented as an adjacency list.
"""

def dfs_iterative(graph, start):
    """
    Perform DFS on a graph from a starting node using an iterative approach.
    
    Parameters:
    graph (dict): A dictionary representing the adjacency list of the graph.
    start (str): The starting node for DFS.
    
    Example:
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    dfs_iterative(graph, 'A')
    """
    visited = set()
    stack = [start]
    
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex)  # Process the vertex (in this case, print it)
            visited.add(vertex)
            
            # Enqueue all adjacent nodes that haven't been visited
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)

# Example usage:
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    dfs_iterative(graph, 'A')

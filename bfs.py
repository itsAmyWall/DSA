# bfs.py

"""
Breadth-First Search (BFS) Algorithm
====================================

Breadth-First Search (BFS) is a fundamental algorithm used for traversing or searching 
through graph or tree data structures.

Characteristics:
----------------
1. Traversal Method: BFS explores nodes level by level. It starts at the root (or an 
   arbitrary node in the case of a graph) and explores all its neighbors at the present 
   depth prior to moving on to nodes at the next depth level.
2. Queue Data Structure: It uses a queue to keep track of the next location to visit.
3. Shortest Path: In an unweighted graph, BFS can be used to find the shortest path from 
   the starting node to any other node.

Steps Involved:
---------------
1. Initialization: Start by enqueueing the root node and marking it as visited.
2. Processing:
   - Dequeue a node from the front of the queue.
   - For each unvisited adjacent node, mark it as visited and enqueue it.
3. Repeat: Repeat the process until the queue is empty.

BFS Algorithm in Pseudocode:
----------------------------
BFS(Graph, start_vertex):
    create a queue Q
    enqueue start_vertex onto Q
    mark start_vertex as visited
    
    while Q is not empty:
        current_vertex = dequeue from Q
        for each neighbor of current_vertex:
            if neighbor has not been visited:
                mark neighbor as visited
                enqueue neighbor onto Q

Example in Python:
------------------
Here's an example of BFS in Python for a graph represented using an adjacency list:
"""

from collections import deque

def bfs(graph, start):
    """
    Perform BFS on a graph from a starting node.
    
    Parameters:
    graph (dict): A dictionary representing the adjacency list of the graph.
    start (str): The starting node for BFS.
    
    Example:
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    bfs(graph, 'A')
    """
    visited = set()          # To keep track of visited nodes
    queue = deque([start])   # Initialize the queue with the start node
    
    while queue:
        vertex = queue.popleft()  # Dequeue a vertex
        if vertex not in visited:
            print(vertex)         # Process the vertex (in this case, print it)
            visited.add(vertex)   # Mark it as visited
            
            # Enqueue all adjacent nodes that haven't been visited
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

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

    bfs(graph, 'A')

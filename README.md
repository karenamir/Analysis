# Analysis
assignment for the Analysis

ass 2
Explanation and time analysis:

- The sequence_alignment function uses dynamic programming to fill a matrix dp where dp[i][j] represents the maximum score for aligning the prefixes x[:i] and y[:j]. The traceback is then performed to find the actual alignment.
- The time complexity of this algorithm is O(mn) since we iterate over each cell in the matrix once.
- The scoring matrix is used to assign scores for matches, mismatches, insertions, and deletions.
- The resulting alignment for the given sequences x and y is printed at the end.

- 
ASS 3
To determine whether an undirected graph is a tree, you need to check two conditions:

Connectedness: A tree is a connected graph, meaning that there is a path between any pair of nodes in the graph.

Acyclic: A tree is an acyclic graph, which means there are no cycles in the graph.

The running time for this algorithm depends on the method. If  a depth-first search (DFS) or breadth-first search (BFS) algorithm, the time complexity would be O(V + E), where V is the number of vertices and E is the number of edges in the graph.
To determine whether an undirected graph is a tree, you need to check two conditions:

1. **Connectedness:** A tree is a connected graph, meaning that there is a path between any pair of nodes in the graph.

2. **Acyclic:** A tree is an acyclic graph, which means there are no cycles in the graph.

You can use a Depth-First Search (DFS) or Breadth-First Search (BFS) to check these conditions:

1. **Connectedness:** Start a DFS or BFS from any node and visit all nodes. If the traversal covers all nodes, the graph is connected.

2. **Acyclic:** During the DFS or BFS, check for the presence of backward edges or cycles. If, at any point, you encounter an already visited node that is not the parent of the current node (in the case of DFS), or if you find a node with more than one parent (in the case of BFS), the graph has a cycle.

The running time of this algorithm is O(V + E), where V is the number of vertices and E is the number of edges in the graph. Both the DFS and BFS traversal take O(V + E) time, and the cycle check adds a constant factor to the time complexity. This is efficient for most practical scenarios, especially when the graph is sparse.

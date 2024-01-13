# Analysis
assignment for the Analysis

ass 2
Explanation and time analysis:

- The sequence_alignment function uses dynamic programming to fill a matrix dp where dp[i][j] represents the maximum score for aligning the prefixes x[:i] and y[:j]. The traceback is then performed to find the actual alignment.
- The time complexity of this algorithm is O(mn) since we iterate over each cell in the matrix once.
- The scoring matrix is used to assign scores for matches, mismatches, insertions, and deletions.
- The resulting alignment for the given sequences x and y is printed at the end.
ASS 3
To determine whether an undirected graph is a tree, you need to check two conditions:

Connectedness: A tree is a connected graph, meaning that there is a path between any pair of nodes in the graph.

Acyclic: A tree is an acyclic graph, which means there are no cycles in the graph.

The running time for this algorithm depends on the method. If  a depth-first search (DFS) or breadth-first search (BFS) algorithm, the time complexity would be O(V + E), where V is the number of vertices and E is the number of edges in the graph.

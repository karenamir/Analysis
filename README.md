# Analysis
assignment for the Analysis

ass 2
Explanation and time analysis:

- The `sequence_alignment` function uses dynamic programming to fill a matrix `dp` where `dp[i][j]` represents the maximum score for aligning the prefixes `x[:i]` and `y[:j]`. The traceback is then performed to find the actual alignment.
- The time complexity of this algorithm is O(mn) since we iterate over each cell in the matrix once.
- The scoring matrix is used to assign scores for matches, mismatches, insertions, and deletions.
- The resulting alignment for the given sequences `x` and `y` is printed at the end.

This program should work with other sequences and scoring matrices as well.

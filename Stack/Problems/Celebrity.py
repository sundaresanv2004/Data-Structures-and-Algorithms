"""
The Celebrity Problem

A celebrity is a person who is known to all but does not know anyone at a party. A party is being organized by some people.
A square matrix mat (n*n) is used to represent people at the party such that if an element of row i and column j is set
to 1 it means ith person knows jth person. You need to return the index of the celebrity in the party, if the celebrity
does not exist, return -1.
Note: Follow 0-based indexing.

Examples:
Input: mat[][] = [[0 1 0], [0 0 0], [0 1 0]]
Output: 1
Explanation: 0th and 2nd person both know 1. Therefore, 1 is the celebrity.

Input: mat[][] = [[0 1], [1 0]]
Output: -1
Explanation: The two people at the party both know each other. None of them is a celebrity.

Input: mat[][] = [[0]]
Output: 0
"""


def celebrity(mat):
    n = len(mat)

    in_deg = [0] * n
    out_deg = [0] * n
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 1:    
                in_deg[j] += 1
                out_deg[i] += 1
    
    for i in range(n):
        if in_deg[i] == n - 1 and out_deg[i] == 0:
            return i

    return -1


matrix = [
    [[0, 1, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0]],
    [[0, 1, 0], [0, 0, 0], [0, 1, 0]],
    [[0, 1, 1], [1, 0, 1], [1, 1, 0]],
    [[0, 1, 1, 0, 0], [0, 0, 1, 0, 0], [0, 1, 0, 0, 0], [0, 1, 1, 0, 0], [0, 1, 1, 0, 0]]
]
for i in matrix:
    print(celebrity(i))

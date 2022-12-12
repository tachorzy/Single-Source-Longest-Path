# Single-Source-Longest-Path
COSC 3320 HW5 Programming Challenge, Professor Wu

Given a weighted acyclic directed graph (DAG) with positive integer weights, and two nodes in the graph i, j, find the longest path from node i -> node j.

Input format:

line 1: [number of nodes N] [number of edges M]<br>
line 2: i j<br>
line 3 to M+2: [node1] [node2] [weight of edge node1->node2]<br>
note: The graph nodes are labeled 0, 1, 2, ..., N-1; all weights are positive integers between 1 and 10000<br>

### Example 1
Input:
4 5<br>
0 3<br>
0 1 10<br>
0 2 20<br>
1 3 30<br>
2 3 15<br>
0 3 60<br>

Output:
60

Explanation:
see the picture below; the longest path from node 0 to node 3 is 60.
![](https://i.ibb.co/FnHJv8Z/dag.png)

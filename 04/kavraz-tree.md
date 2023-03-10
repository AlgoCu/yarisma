Kavraz Tree
Unlike others, this story is actually real!

It is an ordinary day at Istanbul Technical University and Balık is trying to irritate Kavraz as usual. He challenges Kavraz to invent a new type of tree to prove his knowledge of algorithms while expecting him to fail. Trying not to be defeated, Kavraz invents an absurd tree and names it after himself: "Kavraz Tree".

In a Kavraz Tree, levels are defined differently than usual. There are four rules about the levels of a Kavraz Tree:

Any node in the tree has a different level number from its siblings and parent.
Child nodes' levels are greater than parent's level.
The root's level is always 0.
Parent-child relations do not change.
Confident in the absurdity of his tree, Kavraz talks back to Balık, "If you can calculate the minimum level of any given Kavraz tree, then I will agree that you are better at algorithms and Segment Trees than I am".

Can you help Balık to find the minimum level of a given Kavraz tree?

Input Format
First line contains an integer n
 denoting the number of nodes.

The next n−1
 lines contain two integers u
 and v
 indicating an undirected edge between the nodes u
 and v
. All nodes have a unique id in range [0,n−1)
.

Next line contains an integer r
 denoting the root of the tree.

Constraints
1≤n≤105
0≤u,v,r≤n−1
Output Format
Print one integer for the minimum level of the given Kavraz tree.

Sample Input
8
0 2
0 5
1 4
2 3
2 4
4 7
6 4
2
Sample Output
4
Submit Solution
Points:1
Time limit:1.0s
Java2.0s
Java 82.0s
Javascript v83.0s
Mono C#2.0s
Python3.0s
All submissions
Best submissions

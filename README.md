Edmonds-Karp algorithm is used to find the maximum flow of a graph, one key difference between this algorithm 
and Ford's is this one uses a bfs approach while Ford can use a dfs or bfs approach. 


The datastructures used in EdmondsKarp algorithm are:  

lists/arrays: ordered set of elmenets and used in  
-> parent: storing parent node for bfs  
-> visited: storing nodes that have been visited 

adacency matrix: a matrix that is used to represent a graph but with lists or arrays  

queue: First In First Out, used in the bfs to keep track of the nodes visited  

When using edmonds karp algorithm the augmented paths are:  
[0,2,3,1] with a flow of 2  
[0,2,1] with a flow of 1  
and  
[0,2,3,4,1] with a flow of 2  

so when putting in the graph, sink, and source values into the algorithm the output   
for max_flow becomes 5.   



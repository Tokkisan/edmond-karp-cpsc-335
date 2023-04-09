#pseudo code using wikipedia and
# https://brilliant.org/wiki/edmonds-karp-algorithm/ 

#bfs with graph, source, sink 
def bfs(graph, source, sink, parent):
    queue = [source]
    visited = [0] * len(graph)
    visited[source] = 1
    while queue:
        current = queue.pop(0)
        for i, c in enumerate(graph[current]):
            if not visited[i] and c > 0:
                visited[i] = 1
                parent[i] = current
                queue.append(i)
    return visited[sink]


def Edmondskarp(graph, source, sink):
    parent = [-1] * len(graph)
    #set max_flow = 0 
    max_flow = 0
    #call bfs to find shortest path 
    while bfs(graph, source, sink, parent):
        flow = float('inf')
        c = sink
        while c != source:
            flow = min(flow, graph[parent[c]][c])
            c = parent[c]
        c = sink
        
        #while v!= s: 
        while c != source:
            #reducing capacity of augmenting path
            graph[parent[c]][c] = graph[parent[c]][c] - flow
            #increasing the residual capacity of reverse edges
            graph[c][parent[c]] = graph[c][parent[c]] + flow
            c = parent[c]
        #flow:= flow + df
        max_flow += flow
    return max_flow
    



graph = [[0,0,5,0,0],
         [0,0,0,2,0],
         [1,0,4,0,0],
         [0,1,0,2,0],
         [0,3,0,0,0]]

source = 0
sink = 2

print(Edmondskarp(graph, source, sink))


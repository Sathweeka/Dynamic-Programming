'''
BELLMAN FORD ALGORITHM
-------------------------
To find single source shortest path.
disadvantage of dijkistra algorithm is that it is used to find shortest path
but if weight is negative it will not work in that case we have to go for
BELLMAN FORD ALGORITHM.
Drawback of BELLMAN FORD ALGORITHM
------------------------------------
Drawback is when we are having a cycle in graph and its getting negative.
after doing (n-1) iteration also values will change or vertices will relax.
#-------------------------------------------------------------------------
BELLMAN FORD ALGORITHM Disadvantage
-------------------------------------
-> If the given graph is having a cycle and total cost becomes negative
number BELLMAN FORD ALGORITHM won't work.
->Meaning of the sentence "won't work" is after (n-1)th time vertices should
not get relaxed. In the sense, the numbers or cost should not change.
'''
from sys import maxsize
#The row graph[i] represented i-th edge with three values u,v and w.
def BellmanFord(graph,V, E, src):
    #Initialize infinite for all vertices except source
    dis = [maxsize] * V
    #Initialize distance of source as 0
    dis[src] = 0
    #Relax all edges |V| - 1 times. A simple shortest path from src to any
    #other vertex can have atmost |V|-1 edges
    for i in range(V - 1):
        for j in range(E):
            if dis[graph[j][0]] + graph[j][2] < dis[graph[j][1]]:
                dis[graph[j][1]] = dis[graph[j][0]] + graph[j][2]
        #check for negative-weight cycles.
    for i in range(E):
        x=graph[i][0]
        y=graph[i][1]
        weight = graph[i][2]
        if dis[x] != maxsize and dis[x] + weight < dis[y]:
            print("Graph contains negative weight cycle")
    print("Vertex Distance from Source")
    for i in range(V):
        print("%d\t\t%d" % (i, dis[i]))
if __name__ == "__main__":
    V = 5 #Number of vertices in graph
    E = 8 #Number of edges in graph
    #Every edge has 3 values (u, v, w) where the edge is from vertex u to v.
    #And weight of the edge is w.
    graph = [[0,1,-1],[0,2,4],[1,2,3],[1,3,2],[1,4,2],[3,2,5],[3,1,1],[4,3,-3]]
    BellmanFord(graph, V, E,0)

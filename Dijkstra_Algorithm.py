'''
DIJKSTRA ALGORITHM IMPLEMENTATION

find the shortest path from the source

->keep source as 0 and others as infinitythen find the shortest adjacent path
and update its weight as the sum of the before node and the weight. if while
updating the weight is minimum then the previous one then update it with that
but if the weight is greater than the previous one then keep it as it is.

#---------------------------------------------
1) Create a set sptset (shortest path tree set) then keeps track of vertices
included in shortest path tree, i.e., whose minimum distance from source is
calculated and finalized. Initially, this set is empty.

2) Assign a distance value to all vertices in the input graph.
Initialize all distance values as INFINITE.
Assign distance value as 0 for the source vertex so that it is picked first. 

3) While sptSet doesn't include all vertices:

Pick a vertex u which is not there in sptset and has minimum distance value.
Include u to sptset.
Update distance value of all adjacent vertices of u.
To update the distance values, iterate through all adjacent vertices.For every
adjacent vertex v, if the sum of a distance value of u (from source) and weight
of edge u-v, is less than the distance value of v, then update the distance
'''
class Graph():
    def __init__(self, vertices):
        self.v = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]
    def printSolution(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.v):
            print(node, "\t\t", dist[node])
    #function to find the vertex with minimum distance value, from the set of
    #vertices not yet included in shortest path tree
    def minDistance(self, dist, sptSet):
        #Initialize minimum distance for the next node
        min = 1e7#x axis value multiplied by 1e7... like while True its an usage
        #Search not nearest vertex not in the shortest path tree
        for v in range(self.v):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
        return min_index
    def dijkstra(self, src):
        dist = [1e7] * self.v
        dist[src] = 0
        sptSet = [False] * self.v
        for cout in range(self.v):
            #pick the minimum distance vertex from the set of vertices not yet
            #processed. u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)
            #put the minimum distance vertex in the shortest path tree
            sptSet[u] = True
            #update dist value of the adjacent vertices of the picked vertex only
            #if the current distance is greater than new distance and the vertex
            # is not in the shortest path tree
            for v in range(self.v):
                if (self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]
        self.printSolution(dist)
g = Graph(9)
g.graph = [[0,4,0,0,0,0,0,8,0],
           [4,0,8,0,0,0,0,11,0],
           [0,8,0,7,0,4,0,0,2],
           [0,0,7,0,9,14,0,0,0],
           [0,0,0,9,0,10,0,0,0],
           [0,0,4,14,10,0,2,0,0],
           [0,0,0,0,0,2,0,1,6],
           [8,11,0,0,0,0,1,0,7],
           [0,0,2,0,0,0,6,7,0]]
g.dijkstra(0)#source vertex is 0

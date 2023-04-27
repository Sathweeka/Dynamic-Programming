'''
Dynamic programming --- Algorithm
1. GREEDY ALGORITHM
helps to find solution which gives optimized code
helps to find solution which meets the constraints
a> CPU Scheduling algorithms
b> Minimum spanning trees
c> DIJKSTRA SHORTEST Algorithm

Greedy algorithm()
{
for i 1 to n
   if solution = feasible
   solution = solution + 1
optimisation


#----------------------------------------------------
find algorithm:
  find(i)
  {
  while p[i]>0 do
    i=p[i]
  return i
  }

union algorithm:
  union(i,j)
  {
  x=find(i)
  y=find(j)
  if x!=y then
    p[y]=x
  }

ALGORITHM:
MST---KRUSHKAL(G,W)G is graph, W is cost or weight

for each vertex Vertex(G)
   1. do Makeset(v)
   (nothing but we consider every vertex as individual sets)
   2. sort the edges of E in non decreasing order interms of weight
   for each edge (u,v) in sorted order
   3. apply findset for u and v
     if findset(u)!=findset(v) means they are in different set
     so add that as one edge in your MST.
   4. to add you will do union(u,v)
   now this loop you continue for all edges and which all forming cycle will not
   be added.
'''

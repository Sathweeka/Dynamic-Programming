'''
TRAVELLING SALESMAN PROBLEM
-----------------------------------
FORMULAE: starting from 1
g(1,{2,3,4})=min{c1 to any k+g(k,{2,3,4}-{k})}
General formula:
g(i,s)=min{CiK+G(K,S-{K})}
considering subsets minimum path we have to find. If size of S is 2, then S must
C(S,i) = dist(1,i)
Else if size of S is greater than 2.
C(S,i) = min {C(S-{i}, j) + dis(j, i)}
wherej belongs to S, j != i and j != 1
'''
from sys import maxsize
from itertools import permutations
v = 4
#implementation of travelling Salesman Problem....
def travellingSalesmanProblem(graph, s):
    #store all vertex apart from source vertex
    vertex = []
    for i in range(v):
        if i != s:
            vertex.append(i)
    #store minimum weight Hamiltonian Cycle
    min_path = maxsize
    next_permutation=permutations(vertex)
    for i in next_permutation:
        #store current Path weight(cost)
        current_pathweight = 0
        #compute current path weight
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]
        #update minimum
        min_path = min(min_path, current_pathweight)
    return min_path
if __name__ == "__main__":
    #matrix representation of graph
    graph = [[0,10,15,20], [10,0,35,25], [15,35,0,30], [20,25,30,0]]
    s = 0
    print(travellingSalesmanProblem(graph, s))
            

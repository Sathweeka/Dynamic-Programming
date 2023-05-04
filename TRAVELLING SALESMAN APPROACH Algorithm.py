'''
TRAVELLING SALESMAN APPROACH/ TSP / Subset problem            #dunder methods in python
------------------------------------------------------
1<-->2<-->3<-->4<-->1
[[0,10,15,20],[5,0,9,10],[6,13,0,12],[8,8,9,0]]
Dynamic Approach
-----------------
1. Considering no more vertices to visit which means o.
choices
g{4}=8
g{3}=6
g{2}=5
2. Considering one vertex as pending.
choices
g{3,4}=20
g{4,3}=15
g{4,2}=18
g{4,2}=13
g{2,3}=15
g{3,2}=18
3. Considering two vertex as pending.
choices
g{2,3,4}=29
g{2,4,3}=25
g{3,4,2}=25
g{3,4,2}=31
g{4,2,3}=27
g{4,3,2}=23
4. Considering three vertex as pending.
choices
g{1,2,4,3}=35
g{1,3,4,2}=40
g{1,4,2,3}=43
The final minimum cost will be 35 in the direction g{1,2,4,3}
'''

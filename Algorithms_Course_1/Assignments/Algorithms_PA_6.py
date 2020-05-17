import numpy as np

#Initialize largest value of shortest distance to large number
maxDist = 1000000
#Load graph from file and populate Path weight matrix
#Note that if weight for a path is equal to maxDist it means given path is not connected
f = open("djikstra.txt","r")
lines = [line.rstrip('\n').split() for line in f]
Lij = maxDist*np.ones((len(lines),len(lines)),dtype=int)
for g in lines:
    for j in g:
        list = j.split(',')
        if len(list) > 1:
           Lij[lines.index(g)][int(list[0])-1] = int(list[1])
f.close()

#Initialize full graph (use set so that comparison with X can be done irrespective of order 
#in which nodes are captured by algorithm)
V = {i for i in range(1,len(lines)+1)}
# Initialize portion of graph which Djikstra algorithm has already seen
X = {1}
A = {}
A[1] = 0
# Initialize counters
iteration = 0
cnt = 0

while X != V:
    LowDist = maxDist
    LowIdx = 0
    for i in X:
        for j in V:
            if j not in X:
               dist = A[i] + Lij[i-1][j-1]
               cnt += 1
               #print(i,j,dist)
               if dist < LowDist:
                   LowDist = dist
                   LowIdx = j

    X.add(LowIdx)
    A[LowIdx] = LowDist
    iteration += 1

print(iteration,cnt)
print(A[7],A[37],A[59],A[82],A[99],A[115],A[133],A[165],A[188],A[197])

    
#1 - There is a shortest path s-t with no repeated vertices; Shortest path may have as many as n-1 vertices
#2 - When all edges are distinct powers of 2
#3 - Always
#4 - Always terminates but in some cases paths computed will not be shortest; always terminates and in some cases paths computed will be correct shortest path
#5 - Djkistra algorithm always terminates 



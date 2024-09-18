import numpy as np
import time

MAX_VAL = 2**15
def min_path_fw():
   f = open("g3.txt","r")
   params = [line.rstrip('\n')  for line in f]
   f.close()
   
   [num_vertices, num_edges] = params[0].split()
   num_vertices = int(num_vertices)
   num_edges = int(num_edges)

   # Create graph using adjacency matrix
   g = MAX_VAL*np.ones((num_vertices+1, num_vertices+1))
   for i in params[1:]:
    [start, end, cost] = i.split()
    start = int(start)
    end = int(end)
    cost = int(cost)
    g[start][end] = cost
 
   # Initialize cost array. 2D array is sufficient since
   # values at kth iteration are dependent only on (k-1)th
   # iteration
   A = g.copy()
   for i in range(1, num_vertices+1):
    A[i][i] = 0


   # Flyod-Warshell algorithm
   for k in range(1, num_vertices+1):
    for i in range(1, num_vertices+1):
	 #numpy vectorization along j-axis is key to speeding-up computations
	 #using 2D "A" helps only a little-bit
     A[i,:] = np.minimum(A[i,:],np.add(A[i][k], A[k,:]))	
    print(k)

   neg_cycle = False
   for i in range(1, num_vertices+1):
    if A[i][i] < 0:
     neg_cycle = True

   if neg_cycle:
     return "Negative cycle detected"
   else:
     return np.min(A[:,:])

start = time.time()
print(min_path_fw())
print(time.time()-start)





#1 It is a tree with all edges directed away from s
#2 It correctly computes shortest path if and only if the input graph has no negative cost cycles
#3 O(km)  (you can stop bellman-ford algorithm after k iterations)
#4 None of the answers is correct
#5 2^n


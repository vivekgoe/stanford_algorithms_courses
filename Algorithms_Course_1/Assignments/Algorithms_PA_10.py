import numpy as np
import time
from collections import Counter, defaultdict
from bitarray import bitarray
import networkx as nx

def bfs(g, queue, nExplored):
   node = queue.pop()
   #print(g[node])
   for i in g[node]:
      if nExplored[i] == False:
         queue.append(i)
         nExplored[i] = True
         bfs(g, queue, nExplored)

def check_connected(g, edge):
   start_node = edge[0]
   end_node = edge[1]
   #print(g, start_node, end_node)
   queue = [start_node]
   nExplored = np.zeros((len(g),),dtype=np.bool)
   nExplored[start_node] = True
   bfs(g, queue, nExplored)
   
   if nExplored[end_node] == True:
      return 1
   else:
      return 0

def clustering_pb1_naive():
   f = open("clustering1.txt","r")
   params = [line.rstrip('\n')  for line in f]
   f.close()

   # Create empty Graph to keep track of vertices added to MST
   G = []
   for i in range(0,int(params[0])+1):
      G.append(i)
      G[i] = []

   # Add all edges in the graph to a list
   EList = []
   for ln in params[1:]:
      (start_node, end_node, edge_cost) = ln.split()
      EList.append(((int(start_node), int(end_node)),int(edge_cost))) 

   # Sort this list in increasing order of edge cost
   EList.sort(key=lambda tuplee : tuplee[1])
   #print(EList)
   
   T = []
   for i in EList:
       # Check if adding edge "i" to existing MST graph will result in a cycle
       if (check_connected(G, i[0]) == 0):
           # Append new edge to MST
           T.append(i)
           G[i[0][0]].append(i[0][1])
           G[i[0][1]].append(i[0][0])
		   
   return T[len(T)-3][1]

############################################################################################

def combine(g, n1, n2):
   global gD
   start_node = n1
   #print(g, start_node, end_node)
   queue = [start_node]
   nExplored = np.zeros((len(g),),dtype=np.bool)
   nExplored[start_node] = True
   bfs(g, queue, nExplored)
   for i in range(int(len(nExplored))):
       if nExplored[i]:
         gD[i] = gD[n2]

def find(node):
    global gD
    if gD.get(node) == None:
        gD[node] = node
    return gD[node]

def check_connected_uf(g, edge):
    start_node = edge[0]
    end_node = edge[1]
    leader1 = find(start_node)
    leader2 = find(end_node)
    #print(g, gD, start_node, end_node, leader1, leader2) 
    if leader1 == leader2:
       return True
    else:
       combine(g, start_node, end_node)
       return False

gD = {}
def clustering_pb1_fast():
   f = open("clustering1.txt","r")
   params = [line.rstrip('\n')  for line in f]
   f.close()

   # Create empty Graph to keep track of vertices added to MST
   G = []
   for i in range(0,int(params[0])+1):
      G.append(i)
      G[i] = []

   # Add all edges in the graph to a list
   EList = []
   for ln in params[1:]:
      (start_node, end_node, edge_cost) = ln.split()
      EList.append(((int(start_node), int(end_node)),int(edge_cost))) 

   # Sort this list in increasing order of edge cost
   EList.sort(key=lambda tuplee : tuplee[1])
   #print(EList)
   
   T = []
   for i in EList:
       # Check if adding edge "i" to existing MST graph will result in a cycle
       if (check_connected_uf(G, i[0]) == 0):
           # Append new edge to MST
           T.append(i)
           G[i[0][0]].append(i[0][1])
           G[i[0][1]].append(i[0][0])
           #print(len(T))
		   
   return T[len(T)-3][1]

#################################################################################
def bitmasks(n,m):
    if m < n:
        if m > 0:
            for x in bitmasks(n-1,m-1):
                yield bitarray([1]) + x
            for x in bitmasks(n-1,m):
                yield bitarray([0]) + x
        else:
            yield n * bitarray('0')
    else:
        yield n * bitarray('1')


X = nx.utils.UnionFind()
def clustering_pb2():
   gD = {}
   f = open("clustering_big.txt","r")
   params = [line.rstrip('\n')  for line in f]
   f.close()

   for i in range(1,int(params[0].split()[0])+1):
    num = int("".join(params[i].split()), base=2)
    X[i]
    if gD.get(num) == None:
      gD[num] = [i]
    else:
      gD[num].append(i)
      X.union(gD[num][0], i)

   mask0 = [int(b.to01(),base=2) for b in bitmasks(24,1)]
   mask0 = mask0 + [int(b.to01(),base=2) for b in bitmasks(24,2)]

   for d in mask0:
    for i in gD:
     key = i^d
     if key in gD:
      X.union(gD[i][0],gD[key][0])
    #print(d, len(set([X[x] for x in X.__iter__()])))

   pointer_set = set([X[x] for x in X.__iter__()])

   # The number of clusters
   num_clusters = len(pointer_set)	
   return num_clusters   

#start = time.time()
#print(clustering_pb1_naive())
#print(time.time() - start)
start = time.time()
print(clustering_pb1_fast())
print(time.time() - start)
start = time.time()
print(clustering_pb2())
print(time.time() - start)


#1 Both the algorithms may fail.  correct (because its a directed graph)
#2 Both algorithms compute maximum cost spanning tree. But trees may be different.    correct (because ties maybe broken in different way)
#3 The algorithm always output a spanning tree, but it may not be minimum cost spanning tree.   
#4 min bottleneck spanning tree is not minimum spanning but minimum spanning tree is a bottle neck tree.
#5 All are applicable.  correct
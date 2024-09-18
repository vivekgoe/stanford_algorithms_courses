import numpy as np
import time

def job_pb1():
   f = open("jobs.txt","r")
   params = [line.rstrip('\n')  for line in f]
   f.close()

   job_list = []
   for ln in params[1:int(params[0])+1]:
       weight = float(ln.split()[0])
       length = float(ln.split()[1])
       job_list.append((weight - length,weight,length))

   # setting reverse=True sorts in descending order
   # key used for sorting can be a tuple. 1st element of tuple is used for sorting, 2nd element is used in case of tie to break the tie
   # Adding "-" before a tuple element reverses direction of sorting
   job_list.sort(reverse=True, key=lambda tuplee : (tuplee[0],tuplee[1]))
   sum = 0
   completion_time = 0
   for i in job_list:
       completion_time = completion_time + i[2]
       sum = sum + i[1]*completion_time

   return sum

def job_pb2():
   f = open("jobs.txt","r")
   params = [line.rstrip('\n')  for line in f]
   f.close()

   job_list = []
   for ln in params[1:int(params[0])+1]:
       weight = float(ln.split()[0])
       length = float(ln.split()[1])
       job_list.append((weight/length,weight,length))

   job_list.sort(reverse=True, key=lambda tuplee : (tuplee[0],tuplee[1]))

   sum = 0
   completion_time = 0
   for i in job_list:
       completion_time = completion_time + i[2]
       sum = sum + i[1]*completion_time

   return sum

def prim_pb3():
    f = open("edges.txt","r")
    params = [line.rstrip('\n')  for line in f]
    f.close()
    num_nodes = params[0].split()[0]
    num_edges = params[0].split()[1]

    graph = np.NaN*np.ones((int(num_nodes)+1,int(num_nodes)+1))
    for ln in params[1:len(params)]:
        start_node = int(ln.split()[0])
        end_node = int(ln.split()[1])
        edge_weight = int(ln.split()[2])
		# key concept: undirect graph adjacency matrix is symmetric, need to add edge_weight in both direction
		# Note that same will hold for an adjacency list 
        graph[start_node][end_node] = edge_weight
        graph[end_node][start_node] = edge_weight

    X = {i for i in range(1,int(num_nodes)+1)}
    start_node = 1
    V = {start_node}
    X.remove(start_node)
    total_weight = 0
    while len(V) != int(num_nodes):
        min_weight = 1000000000000000
        for i in V:
            for j in X:
                if (np.isnan(graph[i][j]) == False):
                    if (graph[i][j] < min_weight):
                       min_weight = graph[i][j]
                       min_end_node = j
                       min_start_node = i
        V.add(min_end_node)
        X.remove(min_end_node)
        total_weight = total_weight + min_weight
        #print(total_weight, min_weight, min_end_node)

    return total_weight

def Swap(heap,idx1,idx2):
    temp = heap[idx1]
    heap[idx1] = heap[idx2]
    heap[idx2] = temp

def Insert(heap,ele):
    heap.append(ele)
    eidx = heap.index(ele)
    pidx = int((eidx-1)/2)
    while(heap[pidx][0] > heap[eidx][0]):
        Swap(heap,pidx,eidx)
        eidx = pidx
        pidx = int((eidx-1)/2)			

def Extract_Min(heap):
    Swap(heap,0,len(heap)-1)
    ele = heap.pop()
    pidx = 0
    cidx1 = 1
    cidx2 = 2
    while(1):	
       smallest = pidx
       if (cidx1 < len(heap)) and (heap[pidx][0] > heap[cidx1][0]):
          smallest = cidx1
		
       if (cidx2 < len(heap)) and (heap[smallest][0] > heap[cidx2][0]):
          smallest = cidx2
	
       if (smallest != pidx):
          Swap(heap,smallest,pidx)
          pidx = smallest
          cidx1 = 2*pidx+1
          cidx2 = 2*pidx+2
       else:
          break
		
    return ele

def Delete(heap,ele):
    # compute index in heap of node to be deleted
    k = int([i[1] for i in heap].index(ele))
    Swap(heap,k,len(heap)-1)
    ele = heap.pop()
    if (len(heap) == 0) or (k == len(heap)):
       return ele	
    pidx = int((k-1)/2)
    cidx1 = 2*k+1
    cidx2 = 2*k+2
	# shift-up
    if heap[k][0] < heap[pidx][0]:
        eidx = k
        while(heap[pidx][0] > heap[eidx][0]):
            Swap(heap,pidx,eidx)
            eidx = pidx
            pidx = int((eidx-1)/2)
    # shift-down			
    else:
        pidx = k	 
        cidx1 = 2*pidx+1
        cidx2 = 2*pidx+2
        while(1):	
            smallest = pidx
            if (cidx1 < len(heap)) and (heap[pidx][0] > heap[cidx1][0]):
                smallest = cidx1
		
            if (cidx2 < len(heap)) and (heap[smallest][0] > heap[cidx2][0]):
                smallest = cidx2
	
            if (smallest != pidx):
                Swap(heap,smallest,pidx)
                pidx = smallest
                cidx1 = 2*pidx+1
                cidx2 = 2*pidx+2
            else:
                break

    return ele

def heapify(X,V,graph):
    heap = []  
    for j in X:
        min_distance = 10000000
        for i in V:
            if(np.isnan(graph[i][j]) == False):
               min_distance = graph[i][j]
        Insert(heap, (min_distance,j))

    return heap

def prim_heap_impl():
    f = open("edges.txt","r")
    params = [line.rstrip('\n')  for line in f]
    f.close()
    num_nodes = params[0].split()[0]
    num_edges = params[0].split()[1]

    graph = np.NaN*np.ones((int(num_nodes)+1,int(num_nodes)+1))
    for ln in params[1:len(params)]:
        start_node = int(ln.split()[0])
        end_node = int(ln.split()[1])
        edge_weight = int(ln.split()[2])
		# key concept: undirect graph adjacency matrix is symmetric, need to add edge_weight in both direction
		# Note that same will hold for an adjacency list 
        graph[start_node][end_node] = edge_weight
        graph[end_node][start_node] = edge_weight

    start_node = 1
    X = {i for i in range(1,int(num_nodes)+1)}
    X.remove(start_node)
    V = {start_node}
    heap = heapify(X,V,graph)

    total_weight = 0	
    while len(V) != int(num_nodes):
        (dist, node) = Extract_Min(heap)  #find node with min distance
        V.add(node)     #add this node to set V
        X.remove(node)  #remove this node from set X
        total_weight = total_weight + dist
        #print(total_weight, dist, node)
        for j in X:
            if (np.isnan(graph[node][j]) == False):
                ele = Delete(heap, j) #delete from heap any nodes connected to node added to V  
                min_distance = min(ele[0],graph[node][j]) #re-compute min_distance for node j
                Insert(heap, (min_distance, j)) #add node back to heap							
 
    return total_weight 

print(job_pb1())
print(job_pb2())
start = time.time()
print(prim_pb3())
print(time.time() - start)
start = time.time()
print(prim_heap_impl())
print(time.time() - start) 

#5 - for every G and H, these edges are contained in some minimum spanning tree of H
#4 - T is always minimum spanning tree and P may not be always shortest path
#3 - Algorithm A always correctly determines whether a given graph is perfect matching or not; B does not
#2 - Schedule the requests in increasing order of deadline d^j
#1 - At each request pick the remaining request with the earliest finish time





import math
import sys
import heapq as heap
import copy
sys.setrecursionlimit(10**6) 

def huffman_rcrs(num_sym, syms):
    # Base-case, alphabet size of 2
    if num_sym == 2:
       # return a list with tuples of encoded-alphabet & actual alphabet
       return [('1',syms[0][1]), ('0',syms[1][1])]

    syms_local = copy.deepcopy(syms)
	# Pop 2 min weight alphabets from heap
    pa = heap.heappop(syms_local)
    pb = heap.heappop(syms_local)
	# Push new alpabet composed from 2 min weight alphabets
    heap.heappush(syms_local,(pa[0]+pb[0],pa[1]+pb[1]))

    # Recursive call on reduced alphabet set
    syms_ret = huffman_rcrs(num_sym-1, syms_local)
    
    syms_return = copy.deepcopy(syms_ret)
    for j in syms_ret:
       # find min weight alphabets in encoded alphabet list
       if set(pa[1]).issubset(set(j[1])):
	      # add encoded-alphabet, acutal alphabet tuples corresponding to min weight alphabets
          syms_return.append((j[0]+'1',pa[1]))
          syms_return.append((j[0]+'0',pb[1]))
          # delete composite alphabet tuple from list
          syms_return.remove(j)

    # return a list with tuples of encoded-alphabet & actual alphabet
    return syms_return
  
def huffman_pb1():
   f = open("huffman.txt","r")
   params = [int(line.rstrip('\n'))  for line in f]
   f.close()

   # Make a list with weights & alphabet as tuples
   syms = [(i,[j]) for i,j in zip(params[1:],range(1,int(len(params))))]
   # Heapify to a min-heap using weights as key
   heap.heapify(syms)   
 	 
   syms_ret = huffman_rcrs(params[0], syms)
   length_max = 0
   for i in syms_ret:
      length_max = max(length_max,len(i[0]))
	  
   length_min = 100
   for i in syms_ret:
      length_min = min(length_min,len(i[0]))

   return length_min, length_max

def max_weight_pb2():
   f = open("mwis.txt","r")
   params = [int(line.rstrip('\n'))  for line in f]
   f.close()
   
   subsol = []
   a = params[1:]
   subsol.append(0)
   subsol.append(a[0])
   for i,j in zip(a[1:], range(2,len(params))):
     subsol.append(max(subsol[j-1], subsol[j-2] + i))    
   print(a, subsol)

   sol = []
   i = len(a)
   while i >= 1:
     if  subsol[i-1] > a[i-1] + subsol[i-2]:
        i = i-1
     else:
        sol.append(i)
        i = i-2		
 
   print(sol, len(sol))


#print(huffman_pb1())
print(max_weight_pb2())

#1 2230
#2 n-1
#3 If the most frequent letter has frequency less than 0.33, then all letters will be coded with less than 2 bits.
#4 If a vertex is excluded from optimial solution of 2 consecutive subproblems, then it is excluded from the optimal solutions of all bigger subproblems.
#5 The problem is correct in trees, and it leads to efficient dynamic programming algorithm.

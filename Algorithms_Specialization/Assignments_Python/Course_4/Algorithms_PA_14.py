import numpy as np
import time
import math
from bitarray import bitarray

MAX_NUM = 2**16
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

def dist(x , y):
  return np.sqrt((x-y).real*(x-y).real + (x-y).imag*(x-y).imag)


def TSP1():
   f = open("tsp.txt","r")
   params = [line.rstrip('\n')  for line in f]
   f.close()
   
   # populate city co-ordinates
   num_cities = int(params[0])
   city = np.zeros(num_cities, dtype=complex)
   for i in range(0,num_cities):
    real = float(params[i+1].split()[0])
    imag = float(params[i+1].split()[1])
    city[i] = real + imag*1j


   # pre-compute distances between all pairs of cities
   distance = np.zeros((num_cities,num_cities))
   for m in range(0, num_cities):
      distance[m][:] = dist(city[m], city[:])
   
   # total number of sets S
   size = 0
   for m in range(1,num_cities+1):
    size += math.comb(num_cities,m) 
	
   # Initialize base case
   A = MAX_NUM*np.ones((size+1, num_cities))
   for m in range(0,num_cities):
    A[1][m] = 0;

   # Bit-Masks corresponding to each possible set S 
   mask_list = []
   for m in range(2,num_cities+1):
    start = time.time()
    for k in bitmasks(num_cities,m):
     k_int = int(k.to01(),base=2)
     if k_int%2:
      mask_list.append(k)
    print(time.time() - start)
   
   # main algorithm computation loop
   for k in mask_list:    # loop over all sets
    for l, j in enumerate (k.to01()):  # loop over nodes in a set
     if l != num_cities-1 and int(j):
      S_int = int(k.to01(), base=2)
      S_min_l = k.to01()[:l] + '0' + k.to01()[l+1:]    
      S_min_l_int = int(S_min_l,base=2)
      l_prime = num_cities - 1 - l
	  
	  # Inner-most loop vectorized
      a = [int(i) for i in S_min_l]
      a_np = np.array(a)
      p_prime = num_cities - 1 - np.nonzero(a_np)[0]
      A[S_int][l_prime] = np.min(A[S_min_l_int][p_prime] + distance[l_prime][p_prime]) 

   # return to starting node and compute min path length
   minr = MAX_NUM
   for m in range(0,num_cities):
    minr = min((A[size][m] + distance[m][0]), minr)

   return minr

start = time.time()
print(TSP1())
print(time.time() - start)
   
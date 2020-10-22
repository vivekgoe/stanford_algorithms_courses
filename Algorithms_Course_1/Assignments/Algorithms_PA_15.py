import numpy as np
import time

def dist(x , y):
  return np.sqrt((x-y).real*(x-y).real + (x-y).imag*(x-y).imag)

def TSP():
   f = open("nn.txt","r")
   params = [line.rstrip('\n')  for line in f]
   f.close()
   
   num_cities = int(params[0])
   city = np.zeros(num_cities, dtype=complex)
   for i in range(0,num_cities):
    real = float(params[i+1].split()[1])
    imag = float(params[i+1].split()[2])
    city[i] = real + imag*1j
	
   # pre-compute distances between all pairs of cities
   distance = np.zeros((num_cities,num_cities))
   for m in range(0, num_cities):
        distance[m][:] = dist(city[m], city[:])

   a = list(range(1,num_cities))
   dist_min = np.min(distance[0][a])  
   index_min = np.argmin(distance[0][a])
   total = dist_min
   while a:
    index = a[index_min]
    #print(len(a))
    a.remove(index)
    if not a:
     break
    dist_min = np.min(distance[index][a])
    index_min = np.argmin(distance[index][a]) 
    total += dist_min

   return total+distance[index][0]   

start = time.time()
print(TSP())
print(time.time() - start)


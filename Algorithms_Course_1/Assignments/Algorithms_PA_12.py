import numpy as np
import sys

sys.setrecursionlimit(10**6)

def knapsack1():
   f = open("knapsack1.txt","r")
   params = [line.rstrip('\n')  for line in f]
   f.close()

   Capacity = int(params[0].split()[0])
   Items = int(params[0].split()[1])
   #print(Capacity, Items)
   
   v = np.zeros(Items+1)
   w = np.zeros(Items+1)
   for i in range(1,len(params)):
    v[i] = int(params[i].split()[0])
    w[i] = int(params[i].split()[1])
   #print(v,w)

   A = np.zeros((Items+1,Capacity))
   #print(A[0][0])
   for i in range(1,Items+1):
    for x in range(0,Capacity):
      if w[i] > x:
        A[i][x] = A[i-1][x]
      else:	  
        A[i][x] = A[i-1][x]  if (A[i-1][x] > A[i-1][x-int(w[i])]+v[i]) else A[i-1][x-int(w[i])]+v[i] 
    #print(A[i][x])

   return A[Items][Capacity-1]

def knapsack(N, W):
   global v
   global w

   if N == 1:
    return 0.0
	
   if table.get((N,W)) == None:
    max_val_1 = knapsack(N-1, W)
    if int(w[N]) > W:
     table[(N-1,W)] = max_val_1
     return max_val_1
    else:
     max_val_2 = knapsack(N-1, W-int(w[N])) + int(v[N])
     if max_val_1 > max_val_2:
      table[(N-1,W)] = max_val_1
      return max_val_1
     else:
      table[(N-1,W-int(w[N]))] = max_val_2 - int(v[N])
      return max_val_2
   else:
    return table[(N,W)]   

def knapsack2():
   global v
   global w
   global table

   table = {}

   f = open("knapsack_big.txt","r")
   params = [line.rstrip('\n')  for line in f]
   f.close()

   Capacity = int(params[0].split()[0])
   Items = int(params[0].split()[1])

   v = np.zeros(Items+1)
   w = np.zeros(Items+1)
   for i in range(1,len(params)):
    v[i] = int(params[i].split()[0])
    w[i] = int(params[i].split()[1])

   max_val = knapsack(Items, Capacity)
   return max_val

print(knapsack1())
print (knapsack2())


#1 Hint: There is a counterexample with 4 items
   Hint: How do you know it's possible to group the chosen items into subsets S1,S2 into groups of sizes W1, W2
   Neither Algorithm is guaranteed to produce an optimal solution to the problem
   
#2 Hint: Are all the necessary subproblem solutions available for constant time look-up?
   Both algorithms are well-defined and correct after reversing the order of loops.

#3 2.18
#4 All options are correct

#5 Hint: How do you avoid keeping track of \Theta(n^2) subproblem solutions when computing an optimal binary search tree?
   Hint: By throwing away old subproblems that you won't ever need again, you can save space.
   Theta(1), Theta(n), Theta(n^2)




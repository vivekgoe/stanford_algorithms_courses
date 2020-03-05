import numpy as np
from collections import Counter
from collections import deque

def create_graph():
      """ Function that reads pairs of vertices from file and creates 
	      a directed graph (using a Adjacency list) """
      global g
      f = open("scc.txt","r")
      lines = [line.rstrip('\n').split() for line in f]
      f.close()

      # Graph created as list of empty sets
      g = [set() for i in range(0,875715)]
	  # Build adjacency list
      for i in range(0,len(lines)):
          g[int(lines[i][0])].add(int(lines[i][1]))


def reverse_graph():
    """ Function that traverses through adjacency list for a given directed
        graph and creates a equivalent graph with all edges reversed"""
    global g
    global g_rev
	# Graph created as list of empty sets
    g_rev = [set() for i in range(0,875715)]
	# Traverse through each origin vertex
    for i in range(0,len(g)):
        # Traverse through each destination vertex
        for j in g[i]:
            g_rev[j].add(i)

def dfs_rev_stack(i):
    """ Function to execute DFS through reversed graph and order vertices while
        backtracking """
    global nExplored
    global t
    global f
    global f_inv
    nExplored[i] = True
    stack = deque()
    list = deque()
    stack.append(i)
	# Main DFS loop
    while(len(stack)):
        node = stack.pop()
		# Insert elements popped from stack into list to backtrack path traversed during DFS
        list.append(node) 
        for j in g_rev[node]:
            if (nExplored[j] == False):
                stack.append(j)
                nExplored[j] = True
				
    # Traverse through list to figure out topological order of nodes in reversed graph
    while(len(list)):
       t += 1
       temp = list.pop()
	   # Bi-directional mapping using 2 dictionaries
       f[t] = temp
       f_inv[temp] = t

def dfs_stack(i):
    """ Function to execute DFS on original graph """
    global nExplored
    global s
    global leader
    global f
    global f_inv
    nExplored[i] = True
    stack = []
    stack.append(i)
    while(len(stack)):
        node = stack.pop()
        leader[node] = s
        for j in g[f[node]]:
            if (~nExplored[f_inv[j]]):
                stack.append(f_inv[j])
                nExplored[f_inv[j]] = True

# def dfs_rev(i):
    """Recursive implementation to execute DFS through reversed graph"""
    # global nExplored
    # global t
    # global f
    # global f_inv
    # nExplored[i] = True
    # for j in g_rev[i]:
        # if (nExplored[j] == False):
           # dfs_rev(j)

    # t += 1
    # f[t] = i
    # f_inv[i] = t
    # print("f[{}]=".format(t),f[t])

# def dfs(i):
    """Recursive implementation to execute DFS on original graph """
    # global nExplored
    # global s
    # global leader
    # global f
    # global f_inv
    # nExplored[i] = True
    # leader[i] = s
    # for j in g[f[i]]:
        # if (nExplored[f_inv[j]] == False):
           # dfs(f_inv[j])


def dfs_loop():
    """ Main function for finding SCC in a given directed graph"""
    global g
    global g_rev
    global t
    global s
    global f
    global f_inv
    global leader
    global nExplored
    t = 0
    s = 0
    f = {}
    f_inv = {}
    leader = np.zeros((len(g),),dtype=np.int)
    nExplored = np.zeros((len(g),),dtype=np.bool)
    for i in range(len(g)-1,0,-1):
        if nExplored[i] == False:
           dfs_rev_stack(i)

    print("First Pass Finished")
    nExplored = np.zeros((len(g),),dtype=np.bool)    
    for i in range(len(g)-1,0,-1):
        if nExplored[i] == False:
           s = i
           dfs_stack(i)

    # Find leader nodes and member nodes under each leader
    a = Counter(leader)
	# Print 10 largest SCCs
    print(a.most_common(10))

# Create Graph from information given in file
create_graph()
print(len(g))
# Create Reversed Graph
reverse_graph()
print(len(g_rev))
# Run function to find SCCs
dfs_loop()
	  
#Solutions to set 5
#1 - Theta(m)
#2 - Theta(n+m)
#3 - 
#4 -
#5 - 

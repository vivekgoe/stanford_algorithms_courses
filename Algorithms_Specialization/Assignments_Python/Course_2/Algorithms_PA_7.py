def Swap(heap,idx1,idx2):
    temp = heap[idx1]
    heap[idx1] = heap[idx2]
    heap[idx2] = temp

def Max(heap):
    m = max(heap) 
    return heap.index(m)

def Min(heap):
    m = min(heap) 
    return heap.index(m)

def Insert(heap,ele,min):
    """Function to insert a new node to a heap"""
    heap.append(ele)
    eidx = heap.index(ele)
    pidx = int((eidx-1)/2)
    if min:
       while(heap[pidx] > heap[eidx]):
            Swap(heap,pidx,eidx)
            eidx = pidx
            pidx = int((eidx-1)/2)			
    else:
       while(heap[pidx] < heap[eidx]):
            Swap(heap,pidx,eidx)
            eidx = pidx
            pidx = int((eidx-1)/2)

def Extract(heap,min):
    """Function to extract max from minheap or min from maxheap 
	   O(n+logn) where n is size of heap. n operations for 
	   finding max/min index, logn operations for extraction.
	   Note that max element will always be in leaves of binary
	   tree, therefore shift-up required after swap with last 
	   element"""
    if min:
        maxIdx = Max(heap)
        Swap(heap,maxIdx,len(heap)-1)
        eidx = maxIdx
        pidx = int((eidx-1)/2)
        while(heap[pidx] > heap[eidx]):
            Swap(heap,pidx,eidx)
            eidx = pidx
            pidx = int((eidx-1)/2)	
    else:
        minIdx = Min(heap)
        Swap(heap,minIdx,len(heap)-1)
        eidx = minIdx
        pidx = int((eidx-1)/2)
        while(heap[pidx] < heap[eidx]):
            Swap(heap,pidx,eidx)
            eidx = pidx
            pidx = int((eidx-1)/2)			

    return heap.pop()
	
			
# def Extract(heap,min):
    # """Function to extract min or max element, O(logn) operations"""	
    # Swap(heap,0,len(heap)-1)
    # pidx = 0
    # cidx1 = 1
    # cidx2 = 2
    # if min:
       # while (cidx2 < len(heap)):
            # # choose smaller of 2 childs
            # cidx = cidx1 if (heap[cidx1] < heap[cidx2]) else cidx2
            # # swap parent with smaller child if required			
            # if(heap[pidx] > heap[cidx]):			  
                # Swap(heap,pidx,cidx)
                # pidx = cidx
                # cidx1 = 2*pidx+1
                # cidx2 = 2*pidx+2
    # else:
       # while (cidx2 < len(heap)):
            # # choose larger of 2 childs
            # cidx = cidx1 if(heap[cidx1] > heap[cidx2]) else cidx
            # # swap parent with larger child if required
            # if(heap[pidx] < heap[cidx]):			  
                # Swap(heap,pidx,cidx)
                # pidx = cidx
                # cidx1 = 2*pidx+1
                # cidx2 = 2*pidx+1
    
    # return heap.pop()

""" Main code """	
f = open("median.txt","r")
list = [int(line.rstrip('\n')) for line in f]
f.close()
hmin = []
hmax = []

# Trivial case for 1st element
median = list[0]
#print(median)

# Trivial case for 2nd element
if list[0] > list[1]:
   hmin.append(list[1])
   hmax.append(list[0])
   median += list[1]
   #print(median)
else:
   hmin.append(list[0])
   hmax.append(list[1])
   median += list[0]
   #print(median)

for i in range(2,len(list)):
    # Insert new element
    if list[i] <= max(hmin):
       Insert(hmin,list[i],1)
    else:
       Insert(hmax,list[i],0)	

	# Balance between heaps such that each of them is approx. i/2
    if len(hmin)-len(hmax) > 1:
       ele = Extract(hmin,1)
       Insert(hmax,ele,0)
    elif len(hmax)-len(hmin) > 1:
       ele = Extract(hmax,0)
       Insert(hmin,ele,1)
     
    # min heap is smaller, median comes from max heap
    if len(hmax) > len(hmin):
        median += hmax[Min(hmax)]
    # max heap is smaller or both heaps are equal size, median comes from min heap
    else:
        median += hmin[Max(hmin)]
    #print(median,i+1)
    #print(hmin,hmax)

print(median % len(list))


#1 Theta(n) and Theta(1)
#2 Theta(1) and Theta(n)
#3 Find the fifth smallest element stored in the heap
#4 Theta(n)
#5 height of every relaxed red-back tree with n nodes is O(log n)

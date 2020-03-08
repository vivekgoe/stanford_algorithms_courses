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
    pidx = int(eidx/2)
    if min:
       while(heap[pidx] > heap[eidx]):
            Swap(heap,pidx,eidx)
            eidx = pidx
            pidx = int(eidx/2)			
    else:
       while(heap[pidx] < heap[eidx]):
            Swap(heap,pidx,eidx)
            eidx = pidx
            pidx = int(eidx/2)

def Extract(heap,min):
    """Function to extract max from minheap or min from maxheap 
	   O(n+logn) where n is size of heap. n operations for 
	   finding max/min index, logn operations for extraction"""
    if min:
        maxIdx = Max(heap)
        return ExtractI(heap,min,maxIdx)
    else:
        minIdx = Min(heap)
        return ExtractI(heap,min,minIdx)
	
			
def ExtractI(heap,min,pos):
    """Function to extract element with index pos. O(logn) operations"""	
    Swap(heap,pos,len(heap)-1)
    ele = heap.pop()
    if pos > int(ele/2):
       return ele
    pidx = pos
    cidx1 = 2*pidx
    cidx2 = 2*pidx+1
    if min:
       while (pidx > cidx1) or (pidx > cidx2):
           if cidx1 > cidx2:
              Swap(heap,pidx,cidx1)
              pidx = cidx1
           else:
              Swap(heap,pidx,cidx2)
              pidx = cidx2
           cidx1 = 2*pidx
           cidx2 = 2*pidx+1
    else:
       while (pidx < cidx1) or (pidx < cidx2):
           if cidx1 < cidx2:
              Swap(heap,pidx,cidx1)
              pidx = cidx1
           else:
              Swap(heap,pidx,cidx2)
              pidx = cidx2
           cidx1 = 2*pidx
           cidx2 = 2*pidx+1
    
    return ele

""" Main code """	
f = open("heap.txt","r")
list = [int(line.rstrip('\n')) for line in f]
f.close()
hmin = []
hmax = []

# Trivial case for 1st element
median = list[0]
print(median)
#print(hmin,hmax)

# Trivial case for 2nd element
if list[0] > list[1]:
   hmin.append(list[1])
   hmax.append(list[0])
   median += list[1]
   print(median)
   #print(hmin,hmax)
else:
   hmin.append(list[0])
   hmax.append(list[1])
   median += list[0]
   print(median)
   #print(hmin,hmax)
   
for i in range(2,len(list)):
    # Insert every new element to min or max heap
    if list[i] <= hmin[len(hmin)-1]:
       Insert(hmin,list[i],1)
    else:
       Insert(hmax,list[i],0)	

    #print(hmin,hmax)
	# Balance between heaps such that each of them is approx. i/2
    if len(hmin)-len(hmax) > 1:
       ele = Extract(hmin,1)
       Insert(hmax,ele,0)
    elif len(hmax)-len(hmin) > 1:
       ele = Extract(hmax,0)
       Insert(hmin,ele,1)
     
	# median should come from min heap
    if len(hmin) == len(hmax):
        median += hmin[Max(hmin)]
    # min heap is smaller, median comes from max heap
    elif len(hmax) > len(hmin):
        median += hmax[Min(hmax)]
    # max heap is smaller, median comes from min heap
    else:
        median += hmin[Max(hmin)]
    print(median)
    print(hmin,hmax)
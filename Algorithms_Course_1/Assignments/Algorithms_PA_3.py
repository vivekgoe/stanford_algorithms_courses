def Swap(E1,E2):
    temp = E1
    E1 = E2
    E2 = temp
    return E1,E2

def Median(A,l,r):
    """Function to return Median (of 3) element index for a given array"""
	
	#compute center element index
    if (r-l) % 2 == 0:
        center = int((r+l)/2) - 1
    else:
        center = int((r+l)/2)

    #insert left,right and center elements
    list = [A[l],A[r-1],A[center]]
    idx = [l,r-1,center]
    
	#sort 3 element list
    if list[0] > list[1]:
       list[0],list[1] = Swap(list[0],list[1])
       idx[0],idx[1] = Swap(idx[0],idx[1])
    if list[0] > list[2]:
       list[0],list[2] = Swap(list[0],list[2])
       idx[0],idx[2] = Swap(idx[0],idx[2])
    if list[1] > list[2]:
       list[1],list[2] = Swap(list[1],list[2])
       idx[1],idx[2] = Swap(idx[1],idx[2])

    #return index of median element
    return idx[1]
	
def QuickSortM(iArray,Left,Right):
    """Function implmenting QuickSort using Median of 3"""
    global comparisons
    #print(iArray,Left,Right)
    center = Median(iArray,Left,Right)
    iArray[center],iArray[Left] = Swap(iArray[center],iArray[Left])
    r1,l2 = Partition(iArray,Left,Right)
    comparisons += Right-Left-1

    if Left != r1:
        QuickSortM(iArray,Left,r1)
    if l2 != Right:
        QuickSortM(iArray,l2,Right)


def QuickSortL(iArray,Left,Right):
    """Function implementing QuickSort using last element as Pivot"""
    global comparisons
    iArray[Right-1],iArray[Left] = Swap(iArray[Right-1],iArray[Left])
    r1,l2 = Partition(iArray,Left,Right)
    comparisons += Right-Left-1
    if Left != r1:
        QuickSortL(iArray,Left,r1)
    if l2 != Right:
        QuickSortL(iArray,l2,Right)

def QuickSort(iArray,Left,Right):
    """Function implementing QuickSort using first element as Pivot"""
    global comparisons
    #print(iArray)
    r1,l2 = Partition(iArray,Left,Right)
    comparisons += Right-Left-1
    #print(iArray,comparisons, Right, Left)
    if Left != r1:
        QuickSort(iArray,Left,r1)
    if l2 != Right:
        QuickSort(iArray,l2,Right)

def Partition(A,l,r):
    """Function implementing Array Partition step of QuickSort"""
    #print(A,l,r)
    Pivot = A[l]
    i = l+1
    for j in range(l+1,r):
        #print("In:",A,i,j)
        if int(A[j]) < int(Pivot):
           A[i],A[j] = Swap(A[i],A[j])
           i += 1
           #print("Out:",A,i,j)

    A[l],A[i-1] = Swap(A[l],A[i-1])
    return i-1,i

comparisons = 0
if __name__ == '__main__':
    f = open("QuickSort.txt","r")
    sorted = [line.rstrip('\n') for line in f]
    f.close()
    sorted = [int(i) for i in sorted]
    #sorted = [1,5,7,4,3,6]
    QuickSortM(sorted,0,sorted.__len__())
    print(comparisons)

    #sanity check if sorting is correct	
    for i in range(int(sorted.__len__()-1)):
        a = int(sorted[i])
        b = int(sorted[i+1])
        if b - a < 0:
           assert(0)

#Solutions to problem set#3
# 1 - 1-2*alpha
# 2 - -log(n)/log(alpha) <= d <= -log(n)/log(1-alpha)
# 3 - Theta(log(n)); Theta(n)
# 4 - 28
# 5 - Y and Z are not independent; E[YZ] neq E[Y]E{Z]
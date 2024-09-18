import random
import copy

def ContractionRun(List, Size):
    """ Function that runs 1 contraction iteration to find a MinCut starting from random choice of vertex pair"""
	
	# Deepcopy required because List is a "nested list"
	# Each item in List = [item1 = starting vertex, item2 = list of ending vertices]
    InList = copy.deepcopy(List)
    sz = Size
	# Stop when only 2 sub-groups are left
    while sz > 2:
	    #randomly choose vertex (corresponds to row in List)
        n1 = random.choice(range(1,sz))
		#randomly choose another vertex connected to first vertex 
        n2 = random.choice(InList[n1-1][1])   
        #print(n1,n2,InList)
		#iterate over all rows in the List
        for i in range(0,sz):                 
            #print(n2 in InList[i][0])
			#check if choosen vertex pair is connected or not
            if n2 in InList[i][0]:            
			    #combine 2 starting vertices 
                InList[n1-1][0].extend(InList[i][0])   
                #combine 2 lists of ending vertices				
                InList[n1-1][1].extend(InList[i][1])
                #remove both starting vertices from combined list of ending vertices				
                InList[n1-1][1] = [ele for ele in InList[n1-1][1] if ele not in InList[n1-1][0]]
                InList[n1-1][1] = [ele for ele in InList[n1-1][1] if ele not in InList[i][0]]
                del(InList[i])
                sz=sz-1
                #print(InList)
                break
		
	# combined ending vertices list in both sub-groups should be of same size
    assert(len(InList[0][1]) == len(InList[1][1]))		
    #print(InList,len(InList[0][1]),len(InList[1][1]),len(InList[0][0]),len(InList[1][0]))
    return len(InList[0][1])

if __name__ == '__main__':
    f = open("kargerMinCut.txt","r")
    lines = [[line.rstrip('\n').split(maxsplit=1)[0].split(),line.rstrip('\n').split(maxsplit=1)[1].split()] for line in f]
    f.close()
    #lines = [[['1'],['2','4']],[['2'],['3','1']],[['3'],['4','2']],[['4'],['1','3']]]

    #Compute in-degree for each node
    degree = [len(i[1]) for i in lines]
	#Initialize bestmincut to large value (equal to #no of nodes = n)
    bestmincut = 200
	#Run n^2*log(n) times to search for mincut value with high probability 
    for i in range(0,10000):
        #print(lines)
        mincut = ContractionRun(lines,lines.__len__())
        #print(lines)
        #print("iteration:",i,mincut)
        if mincut < bestmincut:
            bestmincut = mincut
            print(i,bestmincut,min(degree))

    # Sanity-check:Bestmincut always less than or equal to min degree 
    print(bestmincut,min(degree))			
	
#Solutions to problem set#4
#1 -  n-1
#2 -  1, 2, 5
#3 -  2*alpha-1
#4 -  -log(n)/log(alpha)
#5 -  n-1


#Final Exam
#1 - 5,9,4
#2 - 2
#3 - Theta(nlog(n))
#4 - Theta(nlog(n)); Theta(n^2)
#5 - All are correct
#6 - 1-2*alpha
#7 - log(epls)/log(1-p)
#8 -  Theta(nk*log(k))
#9 -  Theta(n^log2(7)))
#10 - Rate at which work-per-subproblem is shrinking (per level of recursiion)


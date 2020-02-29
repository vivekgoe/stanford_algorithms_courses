import random
import copy

def ContractionRun(List, Size):

    InList = copy.deepcopy(List)
    sz = Size
    while sz > 2:
        n1 = random.choice(range(1,sz))       #randomly choose vertex
        n2 = random.choice(InList[n1-1][1])   #randomly choose another vertex connected to first vertex 
        #print(n1,n2,InList)
        for i in range(0,sz):                 #iterate over all rows in the list
            #print(n2 in InList[i][0])
            if n2 in InList[i][0]:            #check for second vertex row
                InList[n1-1][0].extend(InList[i][0])   #combine 2 vertices  
                InList[n1-1][1].extend(InList[i][1])   #combine 2 vertices 
                InList[n1-1][1] = [ele for ele in InList[n1-1][1] if ele not in InList[n1-1][0]]        #remove all elements of list[n1-1][0]
                InList[n1-1][1] = [ele for ele in InList[n1-1][1] if ele not in InList[i][0]]       #remove all elements of list[i][0] 
                del(InList[i])
                sz=sz-1
                #print(InList)
                break
		
    assert(len(InList[0][1]) == len(InList[1][1]))		
    #print(InList,len(InList[0][1]),len(InList[1][1]),len(InList[0][0]),len(InList[1][0]))
    return len(InList[0][1])

if __name__ == '__main__':
    f = open("kargerMinCut.txt","r")
    lines = [[line.rstrip('\n').split(maxsplit=1)[0].split(),line.rstrip('\n').split(maxsplit=1)[1].split()] for line in f]
    f.close()
    #lines = [[['1'],['2','4']],[['2'],['3','1']],[['3'],['4','2']],[['4'],['1','3']]]	
    degree = [len(i[1]) for i in lines]
    bestmincut = 200
    for i in range(0,10000):
        #print(lines)
        mincut = ContractionRun(lines,lines.__len__())
        #print(lines)
        #print("iteration:",i,mincut)
        if mincut < bestmincut:
            bestmincut = mincut
            print(i,bestmincut,min(degree))

    print(bestmincut,degree)			
	

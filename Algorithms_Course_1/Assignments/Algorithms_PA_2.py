def merge_and_count_split(aLeft, aRight, aLen):
    i = j = 0
    cnt = 0 
    aSorted = []
    for k in range(aLen):
        if int(aLeft[i]) < int(aRight[j]):
           aSorted.append(aLeft[i])
           i += 1
        else:
           aSorted.append(aRight[j])
           j += 1
           cnt += int(aLeft.__len__())-i 
        
        if aLeft.__len__() == i:
           aSorted.extend(aRight[j:aRight.__len__()])
           break
        elif aRight.__len__() == j:
           aSorted.extend(aLeft[i:aLeft.__len__()])
           break
    
    return aSorted, cnt

def merge_and_count(iArray, iLen):
    if int(iLen) == 1:
        return iArray, 0
    aLeft, iCntLeft = merge_and_count(iArray[0:int(iLen/2)], int(iLen/2))
    aRight, iCntRight = merge_and_count(iArray[int(iLen/2):int(iLen)], int(iLen)-int(iLen/2))
    aSorted, iCntSplit = merge_and_count_split(aLeft, aRight, int(iLen)) 
    return aSorted, (iCntLeft+iCntRight+iCntSplit)

if __name__ == '__main__':
    f = open("IntegerArray.txt","r")
    Input = [line.rstrip('\n') for line in f]
    f.close()
    sorted, invCount = merge_and_count(Input,Input.__len__())
    #print(sorted)
    print(invCount)

    #sanity check if sorting is correct	
    for i in range(int(sorted.__len__()-1)):
        a = int(sorted[i])
        b = int(sorted[i+1])
        if b - a < 0:
           assert(0)


#Solution to problem set#2
#1 - Theta(N^2)
#2 - Theta(n^2 * log(n))
#3 - Theta(n * log3(5)) 
#4 - Theta(b)
#5 - Theta(1)
		   

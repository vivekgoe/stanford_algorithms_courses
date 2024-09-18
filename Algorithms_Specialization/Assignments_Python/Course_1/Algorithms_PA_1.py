import time
import math

count_naive = 0
count = 0
def mul_large_naive(N1, N2):
    global count_naive
    assert(N1.__len__() == N2.__len__())
    len = N1.__len__()
    if len > 1:
        a = N1[0:int(len/2)]
        b = N1[int(len/2):int(len)]
        c = N2[0:int(len/2)]
        d = N2[int(len/2):int(len)]
		#recursive calls
        p1 = mul_large_naive(a,c)
        p2 = mul_large_naive(a,d)
        p3 = mul_large_naive(b,c)
        p4 = mul_large_naive(b,d)
		#merge step;no real multiplication here; only shifts with base 10
        return  10**int(len)*int(p1) + 10**int(len/2)*(int(p2)+int(p3)) + int(p4)
		
    #base case; this is the only real multiplication
    count_naive = count_naive + 1
    assert(N1.__len__() == 1)
    assert(N2.__len__() == 1)
    return int(N1)*int(N2)

def mul_large(N1, N2):
    global count
    assert(N1.__len__() == N2.__len__())
    len = N1.__len__()
    if len > 1:
        p1 = p2 = p3 = 0
        a = N1[0:int(len/2)]
        b = N1[int(len/2):int(len)]
        c = N2[0:int(len/2)]
        d = N2[int(len/2):int(len)]
		#recursive calls
        if int(a) != 0 and int(c) != 0:
            p1 = mul_large(a,c)

        temp1 = str(int(a)+int(b))
        temp2 = str(int(c)+int(d))
        if int(temp1) != 0 and int(temp2) != 0:
           if temp1.__len__() > temp2.__len__():
                tlen = int(math.ceil(math.log2(int(temp1.__len__()))))
                tlen = 2**tlen
                temp1 = '0'*(tlen-temp1.__len__()) + temp1
                temp2 = '0'*(tlen-temp2.__len__()) + temp2
           else:
                tlen = int(math.ceil(math.log2(int(temp2.__len__()))))
                tlen = 2**tlen
                temp1 = '0'*(tlen-temp1.__len__()) + temp1
                temp2 = '0'*(tlen-temp2.__len__()) + temp2
           p2 = mul_large(temp1,temp2)

        if int(b) != 0 and int(d) != 0:
            p3 = mul_large(b,d)
		#merge step;no real multiplication here; only shifts with base 10
        return  10**int(len)*int(p1) + 10**int(len/2)*(int(p2)-int(p1)-int(p3)) + int(p3)
		
    #base case; this is the only real multiplication
    count = count + 1
    assert(N1.__len__() == 1)
    assert(N2.__len__() == 1)
    return int(N1)*int(N2)
		
if __name__ == '__main__':
    Input1 = "3141592653589793238462643383279502884197169399375105820974944592"
    Input2 = "2718281828459045235360287471352662497757247093699959574966967627"
    start = time.time()
    output = mul_large(Input1,Input2)
    print("% s seconds" % (time.time() - start))
    start = time.time()
    output_naive = mul_large_naive(Input1,Input2)
    print("% s seconds" % (time.time() - start))    
    print(output, count)
    print(output_naive,count_naive)
    print(output - output_naive)
    print(output - int(Input1)*int(Input2))
    print(output_naive - int(Input1)*int(Input2))
	
#Solution to Problem Set#1
#1 - nlog(n)
#2 - True
#3 - Sometimes yes, sometimes no (depending on f & g); yes if f(n) <= g(n) for all sufficiently large n
#4 - Omega(nk^2)
#5 - 2^(sqrt(log(n)) < sqrt(n) < n^1.5 < n^(5/3) < 10^n
	

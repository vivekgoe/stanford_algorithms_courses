f = open("2sum.txt","r")
idx = 0
h = set()
for line in f:
   h.add(int(line.rstrip('\n')))
f.close()

cnt = 0
for t in range(-10000,10001):
    flag = False
    for key in h:
        if ((t - key) in h):
            flag = True
            print(key, t-key ,t, cnt)
            break
			
    if flag:
        cnt += 1
		
		
#1 hash function should spread out every data-set
#2 n/m
#3 1/m
#4 n(n-1)/m
#5  
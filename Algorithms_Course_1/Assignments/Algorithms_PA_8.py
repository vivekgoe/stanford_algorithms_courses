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
#5 less than 0.1% (0.045%) 


#1 P definitely remains a shortest s-t path   X
#2 Theta (n+m)   X
#3 Theta(log(n)) and Theta(1)  X
#4 might or might not remain the same (c)
#5 all options are applicable (c)
#6 No option is correct (c)
#7 Theta(n) and Theta(1) (c)
#8 Repeated max computations; repeated min computations (c)
#9 Repeated lookups  (c)
#10 It may or may not compute shortest distances correctly; It always terminates   (c)



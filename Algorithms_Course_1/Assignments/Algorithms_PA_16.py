import Algorithms_PA_5 as scc

def TwoSAT(file_name):
   f = open(file_name,"r")
   params = [line.rstrip('\n')  for line in f]
   f.close()
   
   num_variables = int(params[0])
   f_new = open("sat_graph","w")
   mod = 2*num_variables + 1
   for i in params[1:num_variables+1]:
    elem = [int(j) for j in i.split()]
    f_new.write(str((-1*elem[0]+mod)%mod)+" "+str((elem[1]+mod)%mod)+"\n")
    f_new.write(str((-1*elem[1]+mod)%mod)+" "+str((elem[0]+mod)%mod)+"\n")
   f_new.close()

   scc.create_graph("sat_graph", num_variables*2)
   scc.reverse_graph(num_variables*2)
   (a,b) = scc.dfs_loop()
   
   return b

for i in range(1,7):
  file_name = "2sat"+str(i)+".txt"
  flag = TwoSAT(file_name)
  print(flag)
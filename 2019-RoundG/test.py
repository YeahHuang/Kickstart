#refenced from https://blog.csdn.net/kun768/article/details/43987325

import os
from time import time
import random

correct = "diverseSubarray"
new = "diverseSubarrary_hit_tom"
data = "in.txt"
create_new_data = True
compare_result = False
if create_new_data:
    f = open(data,'w')
    print(20, file=f)
    for i in range(20):
        print(100000, random.randint(1,20), file=f)
        for j in range(100000):
            print(random.randint(1,100000), end=' ', file=f)
        print(file=f)
    f.close()

start = time()
#os.system('python3 %s.py < %s > %s.dat'%(correct, data, correct))
print("Correct time used: ", time()-start)
start = time()
os.system('python3 %s.py < %s > %s.dat'%(new, data,new))
print("New time used: ", time()-start)

if compare_result:
    correct_out = open(correct+'.dat', 'r')
    new_out = open(new+'.dat','r')
    for (i, (a,b)) in enumerate(zip(correct_out, new_out)):
        if a!=b:
            print('line ' + str(i+1))
            print('---AC:'+a)
            print('--NEW:'+b)
print("All done")
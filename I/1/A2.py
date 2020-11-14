import random
import sys

n = int(sys.argv[1])
mySeed = int(sys.argv[2])   
random.seed(mySeed)         # used to customize the initial random number which otherwise is based on the current time 

print(n)

print('_'.join([str(random.randint(1,1000)) for i in range (n)]))
import sys      # to use the argv feature
import os       # to connect model and main solution
import random
#aceept the number of tests as a cmd line parameter
tests = int(sys.argv[1])

#accept the parameter for tests as a cmd line parameter
n = int(sys.argv[2])

for i in range(tests):

    print(f"Test #{i}")
    #run the generator
    os.system(f"A2.py {n} {i} > input.txt")
    #run the model solution
    os.system("maxPairwiseNaive.py < stressInput.txt > model.txt")
    #run the main solution
    os.system("maxPairwiseOptimal.py < stressInput.txt > main.txt")

    #read the ouput of model solution
    with open("model.txt") as f:
        model = f.read()
        print("Model: ", model)
    #read the output of model solution
    with open("main.txt") as f:
        main = f.read()
        print("Main: ", main)
    #break if they don't coincide
    if model != main:
        break
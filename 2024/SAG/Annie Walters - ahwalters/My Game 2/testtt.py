import math
for n in range(1000000):
    if math.sqrt(n*n+(n-2)*(n-2)).is_integer():
        print("n: ",n,"n-2: ",n-2)
import random
import math

n_circle = 0
n_square = 0

for i in range(1000000):
    x = random.random()
    y = random.random()

    if x**2 + y**2 <= 1:
        n_circle += 1
    
    n_square += 1


pi = 4.0 * n_circle / n_square



print("approximate value of pi : {0}".format(pi))
print("exact value of pi: {0}".format(math.pi))


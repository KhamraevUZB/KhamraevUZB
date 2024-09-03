import math

for j in range(998000, 1000000):
    prime = 1
    for i in range(2, int(math.sqrt(j)) + 1):
        if j % i == 0:
            prime = 0
            break
    if prime == 1:
        print(j, end=" ")
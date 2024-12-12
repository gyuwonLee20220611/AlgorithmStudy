import math
n = int(input())

if math.isqrt(n) * math.isqrt(n) == n:
    print(math.isqrt(n))
else:
    print(math.isqrt(n) + 1)
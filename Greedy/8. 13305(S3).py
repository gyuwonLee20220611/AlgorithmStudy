n = int(input())
dst = list(map(int, input().split()))
charge = list(map(int,input().split()))
result = charge[0] * dst[0]
min = charge[0]

for i in range(1,n-1,):
    if min <= charge[i]:
        result += charge[i] * dst[i]
    else:
        min = charge[i]
        result += min * dst[i]
print(result)
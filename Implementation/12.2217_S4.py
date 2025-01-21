n = int(input())
ls = []
for i in range(n):
    ls.append(int(input()))
ls.sort()
result = -1
for i in range(n):
    if ls[i] * (n - i) > ls[-1]:
        result = max(result, ls[i] * (n - i))
if result > 0:
    print(result)
else:
    print(ls[-1])
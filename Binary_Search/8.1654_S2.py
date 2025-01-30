def binary_search(target, start, end):
    if start > end:
        return
    mid = (start + end) // 2
    cnt = 0

    for i in line:
        cnt += i // mid

    if cnt == target:
        result.append(mid)
        return binary_search(target, mid + 1, end)

    elif cnt > target:
        result.append(mid)
        return binary_search(target, mid + 1, end)

    else:
        return binary_search(target, start, mid - 1)

n, k = map(int, input().split())
line = []
result = []
for i in range(n):
    line.append(int(input()))

line.sort()
if sum(line) != k:
    binary_search(k, 0, line[-1])
    result.sort()
    print(result[-1])
else:
    print(1)

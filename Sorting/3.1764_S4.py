n, m = map(int, input().split())
h = []
s = []
ans = []

for i in range(n):
    h.append(str(input()))
for j in range(m):
    s.append(str(input()))

h.sort()
s.sort()

def binary_search(target, start, end):
    if start > end:
        return
    mid =  (start + end) // 2

    if s[mid] == target:
        ans.append(target)
        return

    elif s[mid] > target:
        return binary_search(target, start, mid - 1)

    else:
        return binary_search(target, mid + 1, end)

for i in h:
    binary_search(i, 0, len(s) - 1)


print(len(ans))
for i in ans:
    print(i)


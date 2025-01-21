n = int(input())
ls = list(map(int, input().split()))
num = [0] * 100001
group = []
array = []

for i in ls:
    num[i] += 1
cnt = 0
for j in range(1, len(num)):
    if num[j] // j > 0:
        cnt += num[j] // j

print(cnt)
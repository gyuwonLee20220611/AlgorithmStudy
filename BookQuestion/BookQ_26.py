import heapq

n = int(input())
que = []
result = 0
for i in range(n):
    heapq.heappush(que, int(input()))


if n > 2:

    while que:
        if len(que) == 1:
            break
        num1 = heapq.heappop(que)
        num2 = heapq.heappop(que)
        num_sum = num1 + num2
        heapq.heappush(que, num_sum)
        result += num_sum

    print(result)
elif n == 2:
    num1 = heapq.heappop(que)
    num2 = heapq.heappop(que)
    print(num1 + num2)

else:
    print(0)

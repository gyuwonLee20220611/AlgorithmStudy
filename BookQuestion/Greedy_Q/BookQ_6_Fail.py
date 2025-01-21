import heapq

def solution(food_times, k):
    answer = 0
    que = []

    if sum(food_times) > k:
        for i in range(len(food_times)):
            heapq.heappush(que,(food_times[i], i))

        for i in range(len(food_times)):
            num, idx = heapq.heappop(que)
            k -= num * (len(que) + 1)
            if k < 0:

                break

        answer = k % len(que)


    else:
        answer = -1
    return answer
table = [3, 1, 2]
k = 5
result = solution(table, k)
print(result)
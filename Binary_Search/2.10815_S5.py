n = int(input())
sang = list(map(int, input().split()))
sang.sort()

m = int(input())
card = list(map(int, input().split()))

result = []

def binary_search(array, target, start, end):
    if start > end:
        result.append(0)
        return

    mid = (start + end) // 2

    if len(array) <= mid:
        result.append(0)
        return

    elif array[mid] == target:
        result.append(1)
        return

    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)

    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)


for i in range(len(card)):
    binary_search(sang, card[i], 0, len(sang))


for i in result:
    print(i,end = " ")
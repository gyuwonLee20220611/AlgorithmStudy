def binary_search(array, target, start, end):
    if start > end:
        print(0)
        return
    mid = (start + end) // 2

    if array[mid] == target:
        print(1)
        return

    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)

    else:
        return binary_search(array, target, mid + 1, end)

t = int(input())
for i in range(t):
    n = int(input())
    note_1 = list(map(int, input().split()))
    note_1.sort()
    m = int(input())
    note_2 = list(map(int, input().split()))


    for j in range(m):
        binary_search(note_1, note_2[j], 0, n - 1)
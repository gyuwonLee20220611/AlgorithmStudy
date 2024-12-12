while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    sang = []
    sun = []

    while len(sang) != n:
        a = int(input())
        sang.append(a)

    while len(sun) != m:
        a = int(input())
        sun.append(a)

    result = [0]

    def binary_search(array, target, start, end):
        if start > end:
            return

        mid = (start + end) // 2

        if len(array) <= end:
            return

        elif target == array[mid]:
            result[0] += 1

        elif target > array[mid]:
            return binary_search(array, target, mid + 1, end)

        elif target < array[mid]:
            return binary_search(array, target, start, mid - 1)

    for i in range(len(sun)):
        binary_search(sun, sang[i], 0, m - 1)

    print(result[0])
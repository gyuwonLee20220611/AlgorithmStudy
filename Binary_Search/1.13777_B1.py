def binary_search(array, target, start, end):
    if start > end or target == 0:
        return None
    mid = (end + start) // 2

    if target == array[mid]:
        print(array[mid])
        return None

    elif target > array[mid]:
        print(array[mid], end = ' ')
        return binary_search(array, target, mid + 1, end)

    elif target < array[mid]:
        print(array[mid], end = ' ')
        return binary_search(array, target, start, mid - 1)



envelope = [i + 1 for i in range(50)]
n = -9999999
while n != 0:
    n = int(input())
    binary_search(envelope, n, 0, 49)
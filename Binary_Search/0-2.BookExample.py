n, m = map(int, input().split())
h = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start > end:
        return

    mid = (start + end) // 2
    result = 0
    for i in array:
        if i - mid < 0:
            continue
        else:
            result += i - mid


    if target == result:
        print(mid)

    elif target > result:
        return binary_search(array, target, start, mid - 1)

    else:
        return binary_search(array, target, mid + 1, end)


binary_search(h, m, 0, max(h))
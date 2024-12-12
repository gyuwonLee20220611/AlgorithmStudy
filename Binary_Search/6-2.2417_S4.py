def binary_search(num, start, end):
    if start > end:
        return
    if num == 0:
        print(0)
        return
    elif num == 1:
        print(1)
        return
    mid = (end + start) // 2

    if mid * mid == num:
        print(mid)
        return

    elif mid * mid > num:
        return binary_search(num, start, mid - 1)

    else:
        return binary_search(num, mid + 1, end)


n = int(input())
ls_square = [i*i for i in range()]
binary_search(n, 0, n)
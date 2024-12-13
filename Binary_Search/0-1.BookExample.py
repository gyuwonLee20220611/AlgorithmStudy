n = int(input())
n_ls = list(map(int,input().split()))
n_ls.sort()

m = int(input())
m_ls = list(map(int,input().split()))

def binary_search(array, target, start, end):
    if start > end:
        print("no", end = " ")
        return

    mid = (start + end) // 2

    if array[mid] == target:
        print("yes", end = " ")
        return

    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)

    else:
        return binary_search(array, target, mid + 1, end)


for i in range(m):
    binary_search(n_ls, m_ls[i], 0, n - 1)
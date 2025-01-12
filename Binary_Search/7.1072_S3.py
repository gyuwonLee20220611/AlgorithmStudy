import sys
input = sys.stdin.readline

x, y = map(int, input().split())
z = int(y * 100 / x)
cnt = 1

try:
    if z == 100 or x - y == 1:
        print(-1)
    else:
        while True:
            if z == int((y + cnt) / (x + cnt) * 100):
                cnt *= 2
                continue
            break
        target = z + 1
        start = cnt // 2
        end = cnt
        mid = (start + end) // 2
        while True:
            result = int((y + mid) / (x + mid) * 100)
            if start > end or target == result:
                break
            mid = (start + end) // 2
            if target < result:
                end = mid - 1
            elif target > result:
                start = mid + 1
        print(mid)
        while True:
            a = int((y + mid - 1) / (x + mid - 1) * 100)
            if target == result and target - 1 == a:
                break
            else:
                mid -= 1

        print(mid)
except:
    print(-1)
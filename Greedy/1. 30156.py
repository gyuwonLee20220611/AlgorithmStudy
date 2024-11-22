n = int(input())

for i in range(n):
    str = input()
    a_count = str.count('a')
    b_count = str.count('b')
    if a_count < b_count:
        print(a_count)
    else:
        print(b_count)
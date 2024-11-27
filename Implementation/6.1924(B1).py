m, d = map(int, input().split())
max_day = 0
sum_day = 0

ls = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

for i in range(1,m+1):
    if i == 2 :
        max_day = 28

    elif i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
        max_day = 31

    else:
        max_day = 30

    if i == m:
        sum_day += d

    else:
        sum_day += max_day

week = sum_day%7
print(ls[week])
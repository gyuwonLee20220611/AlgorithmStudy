n = int(input())
sang = list(map(int, input().split()))
m = int(input())
card = list(map(int, input().split()))
result = [0 for i in range(len(card))]

ls_P = [0] * 10000001
ls_M = [0] * 10000001

for i in range(n):
    if sang[i] >= 0:
        ls_P[sang[i]] += 1
    else:
        ls_M[abs(sang[i])] += 1

for i in range(len(card)):
    if card[i] >= 0:
        result[i] = ls_P[card[i]]
    else:
        result[i] = ls_M[abs(card[i])]


for i in result:
    print(i, end = " ")

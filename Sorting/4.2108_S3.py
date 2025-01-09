import math
import sys
input = sys.stdin.readline

n = int(input())
num = []

for i in range(n):
    num.append(int(input()))

num.sort()
#평균
print(round(sum(num) / len(num)))
#중앙값
print(num[len(num)//2])
#최빈값


#범위
print(abs(num[-1] - num[0]))
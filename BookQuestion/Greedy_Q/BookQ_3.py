s = input()
standard = s[0]
cnt =0

for i in s:
    if i != standard:
       cnt += 1
       standard = i
    elif i == standard:
        continue

if cnt % 2 == 1:
    print(cnt//2 + 1)
else:
    print(cnt//2)
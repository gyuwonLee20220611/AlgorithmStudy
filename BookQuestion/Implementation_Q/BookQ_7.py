string = input()
idx = 0
cnt = 0
result = []
for i in range(2):
    for j in range(len(string)//2):
        cnt += int(string[idx])
        idx += 1
    result.append(cnt)
    cnt = 0
if result[0] == result[1]:
    print('LUCKY')
else:
    print('READY')

string = input()
ls = [str(i) for i in range(10)]
cnt = 0
result = ""
for i in sorted(string):
    if i in ls:
        cnt += int(i)

    else:
        result += i

result += str(cnt)
print(result)
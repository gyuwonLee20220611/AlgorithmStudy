string = str(input())
result = 1
for i in string:
    if i == '0':
        result += 0
    elif i == "1":
        result += 0
    else:
        result *= int(i)

print(result)
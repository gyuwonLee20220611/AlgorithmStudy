string = list(map(str, input()))
array = []
integer = ''
reverse = False

for i in range(len(string)):
    if string[i] == '+':
        if not reverse:
            array.append(int(integer))
            integer = ''
        else:
            array.append(-int(integer))
            integer = ''


    elif string[i] == '-' and not reverse:
        array.append(int(integer))
        integer = ''
        reverse = True

    elif string[i] == '-' and reverse:
        array.append(-int(integer))
        integer = ''
        reverse = True

    else:
        integer += string[i]
if reverse:
    array.append(-int(integer))
else:
    array.append(int(integer))

result = 0

for i in array:
    result += i

print(result)

print(array)


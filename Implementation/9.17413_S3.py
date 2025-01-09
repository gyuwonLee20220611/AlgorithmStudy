array = list((map(str, input())))
string = ""
array_1 = []
result = []
reverse = True

for i in range(len(array)):
    if array[i] == '<' or reverse == False:
        result.append(string)
        string = ""
        reverse = False
        string += array[i]


    if array[i] == '>':
        reverse = True
        result.append(string)
        string = ""

    if reverse == True and array[i] != '<' and array[i] != '>':
        if array[i] == ' ':
            result.append(string)
            result.append(' ')
            string = ''

        else:
            string = array[i] + string

result.append(string)

for i in result:
    print(i, end = "")


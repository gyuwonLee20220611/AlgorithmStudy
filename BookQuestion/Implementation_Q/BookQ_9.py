def solution(s):

    ls = [len(s)]
    answer = 0

    for j in range(1, len(s)):
        string = s[0 : j]
        cnt = 1
        result =''
        for k in range(j, len(s), j):
            string2 = s[k : k + j]
            if string == string2:
                cnt += 1
            elif string != string2 and cnt > 1:
                result += str(cnt) + string
                string = string2
                cnt = 1
            else:
                result += string
                string = string2
        if cnt > 1:
            result += str(cnt) + string
        else:
            result += string
        ls.append(len(result))
    print(ls)
    answer = min(ls)
    return answer

s = input()
print(solution(s))
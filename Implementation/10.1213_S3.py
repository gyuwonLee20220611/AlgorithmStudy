string = str(input())
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
dic = {i:0 for i in alphabet}
ls = []
result = ""

for alp in string:
    dic[alp] += 1

for alp in dic:
    if dic[alp] == 1:
        ls.append(alp)

if not len(ls) > 1:


else:
    print("I'm Sorry Hansoo")

print(result)
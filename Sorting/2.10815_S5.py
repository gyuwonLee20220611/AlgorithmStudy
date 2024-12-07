n = int(input())
sang = list(map(int, input().split()))
sang.sort()

m = int(input())
card = list(map(int, input().split()))

result = []

def binary_search(ls, num):
    if ls[0] == num:
        result.append(1)
        return True
    elif len(ls) == 1:
        result.append(0)
        return False


    if ls[len(ls)//2] > num:
        binary_search(ls[0:len(ls) // 2 ], num)

    else:
        binary_search(ls[len(ls) // 2 :], num)



for i in range(len(card)):
    binary_search(sang,card[i])


for i in result:
    print(i,end = " ")

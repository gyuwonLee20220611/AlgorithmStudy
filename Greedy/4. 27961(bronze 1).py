n = int(input())
binary = bin(n)[2:]

if binary.count('1') == 0:
    print(0)

elif binary.count('1') == 1:
    print(len(binary))

else:
    print(len(binary)+1)
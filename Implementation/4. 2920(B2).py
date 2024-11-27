ls = list(map(int, input().split()))
asd = 0
dsd = 0
mix = 0
for i in range(8):
    if ls[i] == i+1:
        asd += 1
    elif ls[i] + i+1 == 9:
        dsd += 1
    else:
        mix += 1

if asd == 8:
    print("ascending")
elif dsd == 8:
    print("descending")
else:
    print("mixed")
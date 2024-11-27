n = int(input())
blank = " "
star = '*'
for i in range(1,2*n,):
    if i <= n:
        print((n-i)*blank, end = "")
        print((i*2-1)*star)
    else:
        print((i-n)*blank, end = "")
        print((2*(n*2-i)-1)*star)
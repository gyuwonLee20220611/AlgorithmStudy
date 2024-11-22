while True:
    try:
        ls = list(map(int, input().split()))

        case1 = ls[1] - ls[0]
        case2 = ls[2] - ls[1]

        if case1 < case2:
            print(case2-1)
        else:
            print(case1-1)
    except:
        break
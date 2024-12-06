array = [5, 7, 9 ,0, 3, 1, 6, 2, 4, 8]

def Quick_sort(start, end):
    pivot = start
    left = start + 1
    right = end - 1

    while left < right:
        if array[pivot] > array[left]:
            left += 1

        elif array[pivot] < array[right]:
            right -= 1

        else:
            array[left], array[right] = array[right], array[left]
            print(array)


    array[right]
    print(array)
    Quick_sort(pivot, right-1)
    Quick_sort(left, end)

Quick_sort(0,len(array))
print(array)
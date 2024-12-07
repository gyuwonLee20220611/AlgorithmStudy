array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def Quick_sort(start, end):
    if start >= end:
        return False
    pivot = start
    left = start + 1
    right = end
    while left <= right:

        while left <= end and array[pivot] >= array[left]:
            left += 1

        while right > start and array[pivot] <= array[right] :
            right -= 1
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    Quick_sort(start, right - 1)
    Quick_sort(right + 1, end)



Quick_sort(0,len(array)-1)
print(array)

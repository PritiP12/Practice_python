def MultiplyByLength(arr):
    length = len(arr)
    for i in range(len(arr)):
        arr[i] = arr[i] * length

    print(arr)
print(MultiplyByLength([2, 3, 1, 0]))
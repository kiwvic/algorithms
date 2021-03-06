def countingSort(arr, grade) -> None:
    divider = 10**grade
    n = len(arr)
    output = [0] * n
    count = [0] * 10
 
    for i in range(n):
        index = int((arr[i] / divider) % 10)
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = int((arr[i] / divider) % 10)
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    for i in range(0, len(arr)):
        arr[i] = output[i]


def radixSort(arr, grade) -> None:
    for i in range(grade):
        countingSort(arr, i)

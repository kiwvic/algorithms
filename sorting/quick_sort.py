def partition(arr, start, end):
    global cnt

    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        cnt += 1
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


def quick_sort(arr, start, end):
    if start < end:
        partition_index = partition(arr, start, end)
        quick_sort(arr, start, partition_index - 1)
        quick_sort(arr, partition_index + 1, end)
    return arr


#####


def partition_median(arr, start, end):
    mid = (start + end) // 2
    global cnt

    if arr[start] <= arr[mid] <= arr[end] or arr[end] <= arr[mid] <= arr[start]:
        arr[mid], arr[end] = arr[end], arr[mid]
    elif arr[mid] <= arr[start] <= arr[end] or arr[end] <= arr[start] <= arr[mid]:
        arr[start], arr[end] = arr[end], arr[start]
    pivot = arr[end]

    i = start - 1
    for j in range(start, end):
        cnt += 1
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1


def quick_sort_median(arr, start, end):
    if start < end:
        if end - start > 3:
            partition_index = partition_median(arr, start, end)
            quick_sort_median(arr, start, partition_index - 1)
            quick_sort_median(arr, partition_index + 1, end)
        else:
            global cnt
            for i in range(start + 1, end + 1):
                j = i - 1
                cnt += 1
                while j >= 0 and arr[j] > arr[j + 1]:
                    arr[j + 1], arr[j] = arr[j], arr[j + 1]
                    j -= 1
    return arr


cnt = 0

name = input("Enter name of file: ")
with open(name, "r") as file:
    lst = [int(i) for i in file.readlines()]
    lst2 = lst.copy()
    with open("is03_Shpachuk_04.txt", "w") as output:
        quick_sort(lst[1:], 0, lst[0] - 1)
        output.write(f"{cnt} ")
        cnt = 0
        quick_sort_median(lst2[1:], 0, lst[0] - 1)
        output.write(str(cnt))
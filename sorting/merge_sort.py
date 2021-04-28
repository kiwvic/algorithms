def merge(left_half: list, right_half: list):
    array = []
    i = 0
    j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            array.append(left_half[i])
            i += 1
        else:
            array.append(right_half[j])
            j += 1
    array.extend(right_half[j:])
    array.extend(left_half[i:])
    return array


def merge_sort(array: list):
    mid = len(array) // 2
    if len(array) == 1:
        return array
    else:
        left_half = merge_sort(array[:mid])
        right_half = merge_sort(array[mid:])
        array = merge(left_half, right_half)
        return array


print(merge_sort([5, 4, 3, 2, 1]))
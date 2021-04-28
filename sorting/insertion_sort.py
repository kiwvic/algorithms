def insertion_sort(lst):
    for i in range(1, len(lst)):
        j = i - 1
        while j >= 0 and lst[j] > lst[j + 1]:
            lst[j + 1], lst[j] = lst[j], lst[j + 1]
            j -= 1
    return lst


print(insertion_sort([4,3,2,1]))
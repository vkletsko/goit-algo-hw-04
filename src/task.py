import timeit
import random


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


variaty = 100  # Can be changed
list_len = 1000  # Can be changed

arr_to_sort = [random.randint(1, variaty) for _ in range(list_len)]

insertion_sort = timeit.timeit(
    "insertion_sort(arr_to_sort.copy())", globals=globals(), number=100
)
merge_sort = timeit.timeit(
    "merge_sort(arr_to_sort.copy())", globals=globals(), number=100
)
timsort_one = timeit.timeit(
    "sorted(arr_to_sort.copy())", globals=globals(), number=100
)
timsort_two = timeit.timeit(
    "arr_to_sort.copy().sort()", globals=globals(), number=100
)

print("\nSorting results\n")
print(
    "{:<24}".format("insertion sort time:"),
    f"{insertion_sort:.6f} sec",
)
print("{:<24}".format("merge sort time:"), f"{merge_sort:.6f} sec")
print("{:<24}".format("built-in sorted() time:"), f"{timsort_one:.6f} sec")
print("{:<24}".format("built-in sort() time:"), f"{timsort_two:.6f} sec")

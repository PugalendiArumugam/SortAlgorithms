def quick_sort(arr):
    if not arr:
        return arr
    if len(arr) <= 1:
        return arr
    # Step 1: Choose a pivot (here, we pick the last element)
    pivot = arr[-1]
    left = []
    right = []
    equal = []

    # Step 2: Partitioning
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            equal.append(num)  # Handles duplicates

    # Step 3: Recursive sorting
    return quick_sort(left) + equal + quick_sort(right)

arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quick_sort(arr)
print(sorted_arr)

def quick_select(arr, k):
    return quick_select_helper(arr, 0, len(arr) - 1, k - 1)

def quick_select_helper(arr, left, right, k):
    if left == right:
        return arr[left]

    pivot_index = partition(arr, left, right)

    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quick_select_helper(arr, left, pivot_index - 1, k)
    else:
        return quick_select_helper(arr, pivot_index + 1, right, k)

def partition(arr, left, right):
    pivot = arr[right]
    i = left

    for j in range(left, right):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[right] = arr[right], arr[i]
    return i

# Example usage
arr = [7, 10, 4, 3, 20, 15]
k = 3
result = quick_select(arr, k)
print(f"{k}th smallest element is: {result}")
k = 5
result = quick_select(arr, k)
print(f"{k}th smallest element is: {result}")

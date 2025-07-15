def bucket_sort(arr):
    n = len(arr)
    if n <= 0:
        return arr

    # Step 1: Create empty buckets
    buckets = [[] for _ in range(n)]

    # Step 2: Put array elements in different buckets
    for num in arr:
        index = int(num * n)  # index range: 0 to n-1
        buckets[index].append(num)

    # Step 3: Sort each bucket
    for i in range(n):
        buckets[i] = sorted(buckets[i])

    # Step 4: Concatenate all buckets into one
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array

def bucket_sort_integers(arr):
    if len(arr) == 0:
        return arr

    # Step 1: Find min and max to determine range
    min_val = min(arr)
    max_val = max(arr)

    # Step 2: Create buckets
    bucket_count = len(arr)
    bucket_range = (max_val - min_val) // bucket_count + 1
    buckets = [[] for _ in range(bucket_count)]

    # Step 3: Distribute numbers into buckets
    for num in arr:
        index = (num - min_val) // bucket_range
        buckets[index].append(num)

    # Step 4: Sort each bucket and concatenate
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(sorted(bucket))  # You can also use insertion sort

    return sorted_array

# Example usage:
arr = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
sorted_arr = bucket_sort(arr)
print("Sorted array:", sorted_arr)
arr = [4, 3, 2, 5,7, 2, 4, 6,1]
sorted_arr = bucket_sort_integers(arr)
print("Sorted array:", sorted_arr)

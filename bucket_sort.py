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

# Example usage:
arr = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
sorted_arr = bucket_sort(arr)
print("Sorted array:", sorted_arr)

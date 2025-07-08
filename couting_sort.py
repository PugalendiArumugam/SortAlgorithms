def counting_sort(arr):
    if not arr:
        return arr

    # Step 1: Find the range
    max_val = max(arr)
    min_val = min(arr)
    range_size = max_val - min_val + 1

    # Step 2: Create count array
    count = [0] * range_size

    # Step 3: Count occurrences
    for num in arr:
        count[num - min_val] += 1

    # Step 4: Calculate positions (cumulative count)
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Step 5: Build the output array
    output = [0] * len(arr)
    for num in reversed(arr):  # reverse to maintain stability
        count[num - min_val] -= 1
        output[count[num - min_val]] = num

    return output

arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print(sorted_arr)

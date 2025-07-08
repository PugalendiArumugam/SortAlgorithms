def majority_element(nums):
    # Step 1: Find candidate
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    # Step 2: Verify candidate
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    else:
        return None

print(majority_element([1,2,1,1,1,2,2,1,1,2,2,2,2,2,1,2,2,2,2,2,1,1,1,1,1,1,1,1,1]))
# print(majority_element([2, 2, 1, 1, 1, 2, 2]))
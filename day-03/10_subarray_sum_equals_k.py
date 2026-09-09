def subarray_sum(nums, k):
    count = 0
    current_sum = 0

    sums = {0: 1}

    for number in nums:
        current_sum += number

        required_sum = current_sum - k

        if required_sum in sums:
            count += sums[required_sum]

        if current_sum in sums:
            sums[current_sum] += 1
        else:
            sums[current_sum] = 1

    return count


nums = [1, 1, 1]
k = 2

print(subarray_sum(nums, k))
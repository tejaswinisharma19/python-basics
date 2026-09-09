def majority_element(nums):
    count = {}

    for number in nums:
        if number in count:
            count[number] += 1
        else:
            count[number] = 1

        if count[number] > len(nums) // 2:
            return number

    return None


nums = [2, 2, 1, 1, 1, 2, 2]

print(majority_element(nums))
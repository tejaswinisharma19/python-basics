def longest_consecutive(nums):
    numbers = set(nums)
    longest = 0

    for number in numbers:

        if number - 1 not in numbers:
            current = number
            count = 1

            while current + 1 in numbers:
                current += 1
                count += 1

            if count > longest:
                longest = count

    return longest


nums = [100, 4, 200, 1, 3, 2]

print(longest_consecutive(nums))
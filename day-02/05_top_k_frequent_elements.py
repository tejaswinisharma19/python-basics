nums = [1, 1, 1, 2, 2, 3]
k = 2

frequency = {}

for num in nums:
    if num in frequency:
        frequency[num] = frequency[num] + 1
    else:
        frequency[num] = 1

result = []

for i in range(k):
    highest = 0

    for num in frequency:
        if frequency[num] > highest:
            highest = frequency[num]
            most_frequent = num

    result.append(most_frequent)
    del frequency[most_frequent]

print(result)
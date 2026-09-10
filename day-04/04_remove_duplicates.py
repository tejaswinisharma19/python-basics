numbers = [0, 0, 1, 1, 2, 2, 3, 3, 4]

position = 1

for i in range(1, len(numbers)):
    if numbers[i] != numbers[i - 1]:
        numbers[position] = numbers[i]
        position += 1

print(numbers[:position])
numbers = [-4, -1, 0, 3, 10]

result = [0] * len(numbers)

left = 0
right = len(numbers) - 1
position = len(numbers) - 1

while left <= right:
    left_square = numbers[left] * numbers[left]
    right_square = numbers[right] * numbers[right]

    if left_square > right_square:
        result[position] = left_square
        left += 1
    else:
        result[position] = right_square
        right -= 1

    position -= 1

print(result)
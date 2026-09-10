numbers = [1, 3, 5, 6]
target = 2

left = 0
right = len(numbers) - 1

while left <= right:
    middle = (left + right) // 2

    if numbers[middle] == target:
        print(middle)
        break

    elif numbers[middle] < target:
        left = middle + 1

    else:
        right = middle - 1
else:
    print(left)
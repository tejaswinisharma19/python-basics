numbers = [-1, 0, 3, 5, 9, 12]
target = 9

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
    print(-1)
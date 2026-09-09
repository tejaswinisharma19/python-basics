def max_area(height):
    left = 0
    right = len(height) - 1
    maximum = 0

    while left < right:

        width = right - left

        if height[left] < height[right]:
            water = height[left] * width
            left += 1
        else:
            water = height[right] * width
            right -= 1

        if water > maximum:
            maximum = water

    return maximum


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

print(max_area(height))
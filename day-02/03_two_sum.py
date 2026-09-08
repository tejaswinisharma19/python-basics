num = [4, 7, 2, 8, 5, 1]
target = 9

for i in range(len(num)):
    for j in range(i + 1, len(num)):
        if num[i] + num[j] == target:
            print(i, j)
            break
def daily_temperatures(temperatures):
    result = [0] * len(temperatures)
    stack = []

    for i in range(len(temperatures)):

        while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
            previous_day = stack.pop()
            result[previous_day] = i - previous_day

        stack.append(i)

    return result


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

print(daily_temperatures(temperatures))
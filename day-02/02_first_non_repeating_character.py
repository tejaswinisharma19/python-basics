s = input()
found = False

frequency = {}

for char in s:
    if char in frequency:
        frequency[char] = frequency[char] + 1

    else :
        frequency[char] = 1

for i in range(len(s)):
    if frequency[s[i]] == 1:
        print(i)
        found = True
        break
        
if not found:
    print(-1)
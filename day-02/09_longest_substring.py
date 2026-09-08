s = input()

characters = set()
left = 0
longest = 0

for right in range(len(s)):
    while s[right] in characters:
        characters.remove(s[left])
        left += 1

    characters.add(s[right])

    if right - left + 1 > longest:
        longest = right - left + 1

print(longest)
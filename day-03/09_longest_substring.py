def longest_substring(s):
    characters = set()

    left = 0
    longest = 0

    for right in range(len(s)):

        while s[right] in characters:
            characters.remove(s[left])
            left += 1

        characters.add(s[right])

        length = right - left + 1

        if length > longest:
            longest = length

    return longest


s = "abcabcbb"

print(longest_substring(s))
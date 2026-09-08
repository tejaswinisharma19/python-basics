s = input()

cleaned = ""

for char in s:
    if char.isalnum():
        cleaned += char

cleaned = cleaned.lower()

if cleaned == cleaned[::-1]:
    print(True)
else:
    print(False)
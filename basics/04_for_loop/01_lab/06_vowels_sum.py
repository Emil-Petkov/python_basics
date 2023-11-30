text = input()

vowels = {
    'a': 1,
    'e': 2,
    'i': 3,
    'o': 4,
    'u': 5
}

sum_of_vowels = 0

for ch in text:
    if ch in vowels:
        sum_of_vowels += vowels[ch]

print(sum_of_vowels)

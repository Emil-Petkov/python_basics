word = input()

vowels_list = {
    'a': 1,
    'e': 2,
    'i': 3,
    'o': 4,
    'u': 5
}
sum_of_vowels = 0

for ch in word:
    if ch in vowels_list:
        sum_of_vowels += vowels_list[ch]

print(sum_of_vowels)

def count_vowels(word):
    char_count = {}
    for char in word:
        if char in "aeoui":
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] = char_count[char] + 1
        else:
            continue
    total_count = 0
    for value in list(char_count.values()):
        total_count += value
    return total_count


# refactored code
# def count_vowels(word):
#     return len([char for char in word if char in 'aeoui'])


# final refactored code
def count_vowels(word):
    return sum(1 for char in word if char in "aeoui")


print(count_vowels("niesdonu"))

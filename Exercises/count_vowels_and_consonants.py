import re
def count_vowels_and_consonants(word):
    count_vowels_consonants = {"vowels":0,"consonants":0}
    only_char = re.sub(r'([^a-zA-z])+',"",word)
    #another option is to use isalpha() method that checks the that every char in a word is alphabet letter
    for char in only_char:
            if char in "aeiou":
                count_vowels_consonants["vowels"] =count_vowels_consonants["vowels"]+1
            else:
                count_vowels_consonants["consonants"] = count_vowels_consonants["consonants"]+1
    return count_vowels_consonants
print(count_vowels_and_consonants("fiekxai1 n!o"))





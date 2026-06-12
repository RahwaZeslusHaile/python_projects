def first_unique_char(word):
    char_count = {}
    for char in word:
        char_count[char] = char_count.get(char,0)+1
    uniqueness =  [key for key in char_count if char_count[key] ==1]
    
    return uniqueness[0] if uniqueness else None
    

            



print(first_unique_char("aabbcdde"))
print(first_unique_char("swiss"))
print(first_unique_char("aabbcc"))
def most_frequent_char(word):
    count_char = {}
    for char in word:
        count_char[char] = count_char.get(char,0)+1
    max_value = max(count_char.values())
    return [k for k, v in count_char.items() if v == max_value]
print(most_frequent_char("hello"))


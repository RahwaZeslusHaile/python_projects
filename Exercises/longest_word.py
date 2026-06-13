def longest_word(sentence):
    separated_word = sentence.split(' ')
    max_word= {}
    for word in separated_word:
        max_word[word] = len(word)
    min_value = max(max_word.values())
    max_key = [k for k,v in max_word.items() if v==min_value ]
    return max_key[0] if max_key[0] else None

print(longest_word("I love Python programming"))
# "programming"

print(longest_word("The quick brown fox"))
# "quick"

print(longest_word(""))
# None
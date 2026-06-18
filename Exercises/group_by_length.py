def group_by_length(words):
    total = {}
    for word in words:
        length_word = len(word)
        if length_word not in total:
            total[length_word] = []
        if word not in total[length_word]:
            total[length_word].append(word)
    return total
    


print(group_by_length(["hi", "cat", "dog", "no", "python"]))
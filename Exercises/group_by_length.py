# def group_by_length(words):
#     total = {}
#     for word in words:
#         length_word = len(word)
#         if length_word not in total:
#             total[length_word] = []
#         total[length_word].append(word)
#     return total


def group_by_length(words):
    total = {}
    for word in words:
        if word not in total.setdefault(len(word), []):
            total[len(word)].append(word)
    return total


print(group_by_length([]))
print(group_by_length(["hi", "cat", "dog", "no", "python"]))
print(group_by_length(["hello"]))
print(group_by_length(["hi", "hi"]))

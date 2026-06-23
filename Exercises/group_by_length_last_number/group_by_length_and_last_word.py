def group_by_length_and_last_letter(words):
    result = {}
    for word in words:
        if word == "":
            continue
        result.setdefault((len(word),word[-1]),[]).append(word)
    return result



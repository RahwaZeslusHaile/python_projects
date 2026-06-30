# def compress_string(text):
#     output_text = ""
#     while len(text) > 0 :
#         count_char = text.count(text[0])
#         output_text = output_text + text[0] + str(count_char)
#         text = text[count_char :]
#     return output_text
# print(compress_string("aaabbc"))
# # "a3b2c1"

# print(compress_string("abcd"))
# # "a1b1c1d1"

# print(compress_string(""))
# # ""


def compress_string(text):
    if not text:
        return ""
    to_be_compared = text[0]
    count = 1
    result = ""

    for char in text[1:]:
        if char == to_be_compared:
            count += 1

        else:
            result += char + str(count)
            to_be_compared = char
            count = 1
    result += char + str(count)
    return result


print(compress_string("aaabbc"))
# "a3b2c1"

print(compress_string("abcd"))
# "a1b1c1d1"

print(compress_string(""))
# ""
print(compress_string("abca"))
# a1b1c1a1

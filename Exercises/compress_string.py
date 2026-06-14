def compress_string(text):
    output_text = ""
    while len(text) > 0 :
        count_char = text.count(text[0])
        output_text = output_text + text[0] + str(count_char)
        text = text[count_char :]
    return output_text
print(compress_string("aaabbc"))
# "a3b2c1"

print(compress_string("abcd"))
# "a1b1c1d1"

print(compress_string(""))
# ""

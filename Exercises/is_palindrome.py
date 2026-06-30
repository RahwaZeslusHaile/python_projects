# def is_palindrome(text):
#     reversed_text = text.replace(" ","").lower()
#     return reversed_text == reversed_text[::-1]

# print(is_palindrome("racecar"))     # True
# print(is_palindrome("level"))       # True
# print(is_palindrome("python"))      # False
# print(is_palindrome("A man a plan a canal Panama"))  # True

# To try writing a palindrome checker without using [::-1].


def is_palindrome(text):
    reversed_text = ""
    for char in reversed(text):
        if char == " ":
            continue
        else:
            reversed_text += char
    return reversed_text.lower() == text.replace(" ", "").lower()


print(is_palindrome("racecar"))  # True
print(is_palindrome("level"))  # True
print(is_palindrome("python"))  # False
print(is_palindrome("A man a plan a canal Panama"))  # True

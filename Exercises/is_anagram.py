# def is_anagram(word1, word2):
#     if len(word1) != len(word2):
#         return False
#     for char in word1:
#         if char not in word2:
#             return False
#         else:
#             index_char = word2.index(char)

#             word2 = word2[:index_char]+ word2[index_char+1:]

#     if len(word2) == 0:
#         return True
#     else:
#         return False
# print(is_anagram("listen", "silent"))  
# print(is_anagram("evil", "vile") )     
# print(is_anagram("hello", "world"))   
# print(is_anagram("aabb", "bbaa"))

# The solution above is passes the expected output but the time complexity is O(n2) because of using index inside the for loop
#I need to improve it
def is_anagram(word1, word2):
    count1 = {}
    count2 = {}
    for char in word1:
        count1[char] = count1.get(char,0)+1
    for char in word2:
        count2[char] = count2.get(char,0)+1
    return count1 == count2
print(is_anagram("listen", "silent"))  
print(is_anagram("evil", "vile") )     
print(is_anagram("hello", "world"))   
print(is_anagram("aabb", "bbaa"))



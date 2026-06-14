
def longest_words(sentence):
    words = sentence.split()
    return list(filter(lambda word:len(word) == len(max(words,key=len)),words))
    
print(longest_words("cat dog sun"))
# ["cat", "dog", "sun"]

print(longest_words("I love Python coding"))
# ["Python", "coding"]

#what I learn
'''
1. Python Iterators & Lazy EvaluationThe 
Concept: Functions like filter() and map() do not return a final list. They return an iterator object (e.g., <filter object>).Lazy Evaluation: The iterator does zero calculations and uses almost zero computer memory when created. It only processes data one item at a time, exactly when requested.The Fix: I must explicitly wrap the iterator in list() (e.g., list(filter(...))) to view, print, or store the final results.Single-Use Rule: Iterators are exhaustible "streams". Once I read through them once, they become empty. Reading them a second time yields an empty list [].

2. The max() Function: Length vs. Alphabetical
The behavior of the max() function changes completely depending on whether I use the key parameter:With key=len: max(words, key=len) evaluates strings based on their character count. It selects the longest word.Without key: max(words) evaluates strings based on alphabetical order (ASCII value). It selects the word that starts with the letter furthest down the alphabet (e.g., "sweet" beats "checolate" because 's' > 'c').

3. Combining filter() and lambda 
I practiced using a lambda (an anonymous, one-line function) inside filter() to scan a list and keep only the elements that match a specific condition—in this case, filtering a list of strings to extract only the ones matching the maximum length.
'''
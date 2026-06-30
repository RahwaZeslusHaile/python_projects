unique_nums = set([1, 2, 2, 3, 3, 3])
print("unique_nums", unique_nums)  # {1,2,3}

unique_words = set(["hi", "hi", "hello"])
print("unique_words", unique_words)  # {"hi","hello"}

unique_nums_range = set(range(0, 8))
print("unique_nums_range", unique_nums_range)  # {0,1,2,3,4,5,6,7}

unique_dic = {"a", "b", "c", "d", "a"}
print("unique_dic", unique_dic)  # {'a','b','c','d'} the order may vary

"""
Why? 

It is a Set, not a Dictionary: Despite the name unique_dic, using curly braces {} with single elements creates a Python set, not a dictionary. Dictionaries require key-value pairs (like {'a': 1}).Duplicates are Removed: Sets automatically filter out duplicate values, so the second 'a' is discarded.
"""

unique_keys = {"a": 1, "b": 2, "c": 3, "d": 4, "a": 5}
print("unique_keys", unique_keys)  # {'a':5,'b':2,'c':3,'d':4}
"""
Keys Must Be Unique: A Python dictionary cannot have duplicate keys.The Last Value Wins: When you define 'a' twice, the second definition ('a': 5) completely overwrites the first one ('a': 1).Order is Preserved: In modern Python (3.7+), dictionaries maintain their insertion order. The key 'a' stays in its original first position, but its value is updated to 5.
"""

unique_keys_only = {"a": 1, "b": 2, "c": 3, "d": 4, "a": 5}

print("unique_keys_only", set(unique_keys_only))  # {'b','c','d','a'}


# add() method
current = {"I", "am", "learning"}
print(current.add("python"))
"""
why None
In Python, the .add() method modifies the set in place. It updates the set directly but does not return the new set. Instead, it returns None.
"""
current_add = {"I", "am", "learning"}
current_add.add("python")
print("current_add", current_add)

# update method
current_add.update("with")
print(
    "current_update", current_add
)  # {'am', 't', 'w', 'learning', 'I', 'python', 'h', 'i'}
"""
The .update() method expects an iterable (like a list, set, or tuple) and adds each item from that iterable one by one. When you pass a single string like 'with', Python treats the string as a list of individual characters ('w', 'i', 't', 'h') and adds each letter separately."""

current_add.update(["with", "passion"])
print(
    "current_update_list", current_add
)  # {'passion', 'learning', 'with', 't', 'python', 'I', 'i', 'h', 'am', 'w'}

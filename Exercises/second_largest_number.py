def second_largest(numbers):
    sorted_numbers = sorted(set(numbers))
    return sorted_numbers[-2] if len(sorted_numbers) >= 2 else None


print(second_largest([1, 5, 3, 9, 2]))
# 5

print(second_largest([10, 10, 8, 7]))
# 8

print(second_largest([5]))
# None)

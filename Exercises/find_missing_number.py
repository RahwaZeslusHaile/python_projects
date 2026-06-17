def find_missing_number(numbers):
    numbers.sort()

    missing = next(
        (i + 1 for i in range(len(numbers))
         if numbers[i] != i + 1),
        None
    )

    return missing if missing is not None else len(numbers) + 1

        
    


print(find_missing_number([1, 2, 4, 5]))
# 3
print(find_missing_number([2, 3, 4, 5]))
# 1

print(find_missing_number([2, 3, 1, 5]))
# 4

print(find_missing_number([1]))
# None


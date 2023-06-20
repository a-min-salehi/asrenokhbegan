count_vowels = lambda string: sum(1 for char in string if char.lower() in 'aeiou')

result = count_vowels("Hello, World!")
print(result)  # Output: 3

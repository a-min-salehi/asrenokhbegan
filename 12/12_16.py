count_vowels = lambda string: sum(1 for char in string if char.lower() in 'aeiou') # (1,1,1,1)

result = count_vowels("Hello, World!")
print(result)  # Output: 3

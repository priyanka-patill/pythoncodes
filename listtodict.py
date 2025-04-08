# Sample list
words = ['apple', 'banana', 'cherry']

# Convert to dictionary with indices as keys
word_dict = {index: word for index, word in enumerate(words)}

print(word_dict)

{0: 'apple', 1: 'banana', 2: 'cherry'}

# Sample list
words = ['apple', 'banana', 'cherry']

# Convert to dictionary with words as keys and lengths as values
word_dict = {word: len(word) for word in words}

print(word_dict)

{'apple': 5, 'banana': 6, 'cherry': 6}

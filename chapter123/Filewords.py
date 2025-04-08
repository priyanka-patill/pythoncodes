f = open("demofile.txt", "r")
paragraph = f.read()
words = paragraph.split()
print(words)
print(type(words))

def count_word_lengths(words):
    # Create a dictionary to store word lengths and their counts
    word_lengths = {}
    
    for word in words:
        length = len(word)
        if length in word_lengths:
            word_lengths[length] += 1
        else:
            word_lengths[length] = 1
    
    return word_lengths

word_lengths = count_word_lengths(words)

print("Word lengths and their counts:")
for length, count in word_lengths.items():
    print(f"Length {length}: {count} words")

for length in word_lengths:
    # Filter words of the current length
    words_of_length = [word for word in words if len(word) == length]
    print(f"Length {length}: {', '.join(words_of_length)}")


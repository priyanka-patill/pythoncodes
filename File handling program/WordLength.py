def get_words_of_length(file_path, lengths):
    # Initialize a dictionary to store words of specified lengths
    words_of_length = {length: [] for length in lengths}

    # Read the file and process each word
    with open('demofile.txt', 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                # Remove punctuation and convert to lowercase
                word = ''.join(char.lower() for char in word if char.isalnum())
                if len(word) in words_of_length:
                    words_of_length[len(word)].append(word)

    # Print words of each specified length
    for length in lengths:
        print(f"Words of length {length}:")
        print(", ".join(words_of_length[length]))
        print("\n")

# Example usage
file_path = 'demofile.txt'
f = open("demofile.txt", "r")
print(f.read())
lengths = [3, 4, 5, 6,7,8,9]
get_words_of_length(file_path, lengths)

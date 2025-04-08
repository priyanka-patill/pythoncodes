def sort_words_by_length(words):
    # Create a dictionary to store words with their lengths as keys
    length_dict = {}
    for word in words:
        length = len(word)
        if length in length_dict:
            length_dict[length].append(word)
        else:
            length_dict[length] = [word]
    
    # Sort the dictionary by length
    sorted_words = sorted(length_dict.items(), reverse='True')
    print(sorted_words)
    
    # Convert the sorted dictionary back to a list of words
    sorted_list = []
    for length, words in sorted_words:
        sorted_list.extend(words)
    
    return sorted_list

# Example usage
words = ["apple", "banana", "cherry", "date", "fig", "grape"]
sorted_words = sort_words_by_length(words)
print(sorted_words)

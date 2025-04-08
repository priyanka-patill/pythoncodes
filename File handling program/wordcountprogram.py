f = open("wordcount.txt", "r")
paragraph = f.read()
#line = "Hello, this is an example line."
words = paragraph.split()
print(words)
print(type(words))
p=[]
for x in words:
    p.append(x)
   

print(p)

 # Create a dictionary to store word lengths and their counts
wlength = {}
    
for x in words:
     length = len(x)
     #print(length)
     if length in wlength:
          wlength[length] += 1        
     else:
         wlength[length] = 1
         
        
    
print(wlength)


def segregate_words_by_length(words):
    word_dict = {}
    for word in words:
        length = len(word)
        if length not in word_dict:
            word_dict[length] = []
        word_dict[length].append(word)
    return word_dict


segregated_words = segregate_words_by_length(words)
print(segregated_words)











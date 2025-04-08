f = open("wordcount.txt", "r")
paragraph = f.read()
#line = "Hello, this is an example line."
words = paragraph.split()
print(words)
print(type(words))

   



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



wd = {}
for word in words:
    length = len(word)
    if length not in wd:
        wd[length] = []         
    wd[length].append(word)
print(wd)




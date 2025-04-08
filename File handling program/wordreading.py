f = open("demofile.txt", "r")
paragraph = f.read()
#line = "Hello, this is an example line."
words = paragraph.split()
print(words)
print(type(words))
print(len(words))



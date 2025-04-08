# Opening a file for reading
file = open("demofile.txt", "r")
content = file.read()
print(content)



with open("demofile.txt", "r") as file:
    content = file.read()
    print(content)

"""
Reading from a File
You can read the contents of a file using various methods:

read(): Reads the entire file

readline(): Reads one line at a time

readlines(): Reads all lines and returns them as a list
"""
with open("demofile.txt", "r") as file:
    content = file.readline()
    print(content)

with open("demofile.txt", "r") as file:
    content = file.readlines()
    print(content)
    print(len(content))

    """
Writing to a File
You can write to a file using the write() or writelines() methods:
"""
    with open("example.txt", "w") as file:
        file.write("Hello, world!")
     
    with open("example.txt", "a") as file:
        file.write("Which place to watch for!")
     


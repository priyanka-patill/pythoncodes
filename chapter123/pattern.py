
n= int (input ("Enter the number of Rows"))
for i in range(n):
    for j in range(n-i):
        print("", end = " ")
    for k in range(i+1):
        print(chr(k+65),  end ="")
    for l in range(i):
        print(chr(l+65), end="")
    print()




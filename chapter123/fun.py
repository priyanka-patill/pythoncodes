"""
def sum(x,y):
    print(x+y)
sum(2,3)

sum= lambda x,y:x+y
print(sum(2,3))
    
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i      
    print(f)
fact(5)
"""
fact=lambda f=1,n:if n <= 1 else num*fact(n-1)
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

fact=lambda n : 1 if n <= 1 else n*fact(n-1)
print(fact(5))
"""
fact=lambda  n, f=1 : [f := f * i for i in range(1, n + 1)][-1]
print(fact(5))

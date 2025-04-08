class A:
    def info(self):
        print("I am Professor in IT Department")

        

class B:
    def name(self):
        print("Myself Dr. Arun Kulkarni")


class C(A,B):
    pass

# create an object of Bat class
b1 = C()

b1.name()
b1.info()

# Base Class
class Vehicle:
    p=0
    stock=25
    
    def __init__(self,vt,rp):
        self.vt =vt
        self.rp=rp
    def VA(self):
        print(f"The available {self.vt} are {self.stock} with rent of Rs {self.rp} per day of {self.agency} agency")
        
# Derived CLass
class rentalagencies(Vehicle):
    def __init__(self,agency,vt,rp):
        self.agency = agency
        Vehicle.__init__(self,vt,rp)
    def Rentalperiod(self):        
        p=int(input("Enter the period"))
        return (p)
        
# Derived Class
class rentaltransition(rentalagencies):
    def __init__(self,agency,vt,stock,rp):
        self.stock=stock        
        rentalagencies.__init__(self,agency,vt,rp)
    def pb(self,p1,price,number):
        self.p1=p1
        self.price=price
        self.number=number
        amount=self.p1*self.price*self.number
        return amount
 

print(" 1:Information 2:For First agency 3:for second agency 4:Exit")
choice=int(input("Enter the choice"))

while (True):
    if choice==1:
        v1 = rentaltransition("star","Cars",20,25)
        v1.VA()
        v2 = rentaltransition("Royal","Cars",25,10)
        v2.VA()
        break
         
  
    elif choice == 2:
        d=int(input("Enter the number of cars"))
        v1 = rentaltransition("star","Cars",10,25)
        p1=v1.Rentalperiod()
        
        am=v1.pb(p1,25,d)
        print(f"Your order for {d} Cars is booked.Please pay Rupees{am}")
        break
    elif choice == 3:
        print("continue")
        y="True"
        break
    else:
        print("Not interested")
        break

  


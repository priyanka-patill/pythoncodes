"""
Develop classes for products, customers, and shopping carts.
Include methods for adding items to the cart, calculating total costs, processing orders,
and managing inventory.
"""
# Base Class
class product:
    
    def additemstocart(self, item,x,q,quantity):
        self.x=x
        self.item=item
        self.q=q
        self.quantity=quantity
        self.x.append(self.item)
        self.q.append(self.quantity)
        return[self.x, self.q]
 
        
        
# Derived CLass
class customers(product):
    def add(self, name):
        self.name=name
        listofcustomers.append(self.name)
        # print(y)
    
       
        
# Derived Class
class shoppingcart(customers):
    def billing(self,fa,amount,aa):
        self.amount=amount
        self.fa=fa
        self.aa=aa
        ab = [self.fa[i]*self.aa[i] for i in range(len(self.aa))]
        
        self.amount=sum(ab)
        return (self.amount)
      
        
q=[]
x=[]
listofcustomers=[]
bill=[]
v3=shoppingcart()
amount=0
i=1
while(i<=20):
      i=i+1
      print(" Available shopping items available")
      A={"Rice":51, "sunflower oil": 150, "choclate":100}
      print(A)
      print(" ---------------------------------------------------------------------------------------")
      print(" ---------------------------------------------------------------------------------------")
      v2=shoppingcart()
      name=input(" please enter your name")
      v2.add(name)
      print(" ---------------------------------------------------------------------------------------")
      print(" ---------------------------------------------------------------------------------------")
      print(" Please choose the option for shopping")
      print("1: adding the items, 2:Billing")
     
      while (True):
          if( i==25):
              
              break
          
          
         
          choice=int(input("Enter the choice"))      
                               
          if choice==1:
              
               v1=shoppingcart()
               print(" Please enter the items as per the  Menu to the Cart")
               print("1:Rice\t 2:sunfloweroil\t 3:choclate")
               ch=int(input("Enter the item"))
               quantity=int(input("Enter the quantity"))  
               f=v1.additemstocart(ch-1,x,q,quantity)
               
               print(" ---------------------------------------------------------------------------------------")
               print(" whether you want to 1:add the items2:Billing")

                        
                      
          elif choice == 2:
              
              fa=[]
              
              
              for i in f[0]:
                 key = list(A.keys())[i]
                 value=A[key]
                 
                 fa.append(value)
    
              am=v3.billing(fa, amount,f[1])
              bill.append(am)
              print(f"Mr.{name}  bill amount is Rupees {am}")
              print(" Thank you for shopping")
              print(listofcustomers)
              print(bill)
              i=25
               
                
                               
                            
      
                
              
                              
                      
                                
             
                                

    
          
                
  


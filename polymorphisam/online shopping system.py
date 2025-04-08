"""
Develop classes for products, customers, and shopping carts.
Include methods for adding items to the cart, calculating total costs, processing orders,
and managing inventory.
"""
# Base Class
class product:
    
    def additemstocart(self, item,x):
        self.x=x
        self.item=item
       
        self.x.append(self.item)
        return(self.x)
 
        
        
# Derived CLass
class customers(product):
    def add(self, name):
        self.name=name
        y.append(self.name)
        print(y)
    
       
        
# Derived Class
class shoppingcart(customers):
    def billing(self,fa,amount):
        self.amount=amount
        self.fa=fa        
        self.amount=sum(self.fa)
        return (self.amount)
        
        

x=[]
y=[]
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
               print("1:Rice\n 2:sunfloweroil\n 3:choclate")
               ch=int(input("Enter the item"))  
               f=v1.additemstocart(ch-1,x)
               print(" ---------------------------------------------------------------------------------------")
               
               print(" whether you want to add the items")

                        
                      
          elif choice == 2:
              
              fa=[]
              
              
              for i in f:
                 key = list(A.keys())[i]
                 value=A[key]
                 
                 fa.append(value)
    
              am=v3.billing(fa, amount)
              print(f"Your bill amount is Rupees {am}")
              print(" Thank you for shopping")
              i=25
               
                
                               
                            
      
                
              
                              
                      
                                
             
                                

    
          
                
  


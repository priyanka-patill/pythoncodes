
class vehicle:
    print ("This is a Car rental system")
    print("-----------------------------------")
class rentalagencies:
        def __init__(self, name, email, cartype, stock, rent):
            self.name = name
            self.email = email
            self.cartype=cartype
            self.stock=stock
            self.rent=rent
            print(" Details of the vendor are")
            print(f" {self.name} with email {self.email} and car is {self.cartype} and  stock available is{stock}with rent {self.rent} per day")

y1=rentalagencies("xyz", "aaa@gmail.com"," Ford",50, 1000)
y2=rentalagencies("ABK", "ppp@gmail.com"," Honda",150, 2000)
    

class Vehicle:
    def __init__(self, vehicle_id, make, model, year, price_per_day):
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.year = year
        self.price_per_day = price_per_day
        self.available = True

    def __str__(self):
        return f"{self.year} {self.make} {self.model} (ID: {self.vehicle_id})"


class RentalTransaction:
    def __init__(self, transaction_id, vehicle, customer_name, rental_period):
        self.transaction_id = transaction_id
        self.vehicle = vehicle
        self.customer_name = customer_name
        self.rental_period = rental_period
        self.total_cost = self.calculate_cost()

    def calculate_cost(self):
        return self.vehicle.price_per_day * self.rental_period

    def __str__(self):
        return f"Transaction {self.transaction_id}: {self.vehicle} rented by {self.customer_name} for {self.rental_period} days. Total cost: ${self.total_cost}"


class RentalAgency:
    def __init__(self, name):
        self.name = name
        self.vehicles = {}
        self.transactions = {}
        self.next_vehicle_id = 1
        self.next_transaction_id = 1

    def add_vehicle(self, make, model, year, price_per_day):
        vehicle = Vehicle(self.next_vehicle_id, make, model, year, price_per_day)
        self.vehicles[self.next_vehicle_id] = vehicle
        self.next_vehicle_id += 1
        print(f"Vehicle added: {vehicle}")

    def list_available_vehicles(self):
        return [vehicle for vehicle in self.vehicles.values() if vehicle.available]

    def rent_vehicle(self, vehicle_id, customer_name, rental_period):
        if vehicle_id not in self.vehicles:
            print("Vehicle not found.")
            return

        vehicle = self.vehicles[vehicle_id]
        if not vehicle.available:
            print("Vehicle is not available.")
            return

        vehicle.available = False
        transaction = RentalTransaction(self.next_transaction_id, vehicle, customer_name, rental_period)
        self.transactions[self.next_transaction_id] = transaction
        self.next_transaction_id += 1
        print(f"Rental transaction created: {transaction}")

    def return_vehicle(self, transaction_id):
        if transaction_id not in self.transactions:
            print("Transaction not found.")
            return

        transaction = self.transactions[transaction_id]
        vehicle = transaction.vehicle
        vehicle.available = True
        print(f"Vehicle returned: {vehicle}")

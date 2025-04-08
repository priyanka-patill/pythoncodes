def rupees_to_dollars(rupees, exchange_rate):
    return rupees / exchange_rate

def dollars_to_rupees(dollars, exchange_rate):
    return dollars * exchange_rate

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def inches_to_feet(inches):
    return inches / 12

def feet_to_inches(feet):
    return feet * 12

def main():
    while True:
        print("\nConverter Menu:")
        print("1. Rupees to Dollars")
        print("2. Dollars to Rupees")
        print("3. Celsius to Fahrenheit")
        print("4. Fahrenheit to Celsius")
        print("5. Inches to Feet")
        print("6. Feet to Inches")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            rupees = float(input("Enter amount in Rupees: "))
            exchange_rate = float(input("Enter current exchange rate (1 Dollar to Rupees): "))
            print(f"Amount in Dollars: {rupees_to_dollars(rupees, exchange_rate):.2f}")
        elif choice == '2':
            dollars = float(input("Enter amount in Dollars: "))
            exchange_rate = float(input("Enter current exchange rate (1 Dollar to Rupees): "))
            print(f"Amount in Rupees: {dollars_to_rupees(dollars, exchange_rate):.2f}")
        elif choice == '3':
            celsius = float(input("Enter temperature in Celsius: "))
            print(f"Temperature in Fahrenheit: {celsius_to_fahrenheit(celsius):.2f}")
        elif choice == '4':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            print(f"Temperature in Celsius: {fahrenheit_to_celsius(fahrenheit):.2f}")
        elif choice == '5':
            inches = float(input("Enter length in Inches: "))
            print(f"Length in Feet: {inches_to_feet(inches):.2f}")
        elif choice == '6':
            feet = float(input("Enter length in Feet: "))
            print(f"Length in Inches: {feet_to_inches(feet):.2f}")
        elif choice == '7':
            print("Exiting Converter.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

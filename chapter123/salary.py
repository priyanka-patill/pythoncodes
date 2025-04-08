
"""def calculate_gross_salary(basic_salary):
    da = 0.70 * basic_salary
    ta = 0.30 * basic_salary
    hra = 0.10 * basic_salary
    gross_salary = basic_salary + da + ta + hra
    return da, ta, hra, gross_salary

def main():
    basic_salary = float(input("Enter the basic salary (BS): "))
    da, ta, hra, gross_salary = calculate_gross_salary(basic_salary)
    
    print(f"Dearness Allowance (DA): {da:.2f}")
    print(f"Travel Allowance (TA): {ta:.2f}")
    print(f"House Rent Allowance (HRA): {hra:.2f}")
    print(f"Gross Salary: {gross_salary:.2f}")

if __name__ == "__main__":
    main()
"""
basic_salary = float(input("Enter the basic salary (BS): "))
da = 0.70 * basic_salary
ta = 0.30 * basic_salary
hra = 0.10 * basic_salary
gross_salary = basic_salary + da + ta + hra
print(f"Dearness Allowance (DA): {da:.2f}")
print(f"Travel Allowance (TA): {ta:.2f}")
print(f"House Rent Allowance (HRA): {hra:.2f}")
print(f"Gross Salary: {gross_salary:.2f}")


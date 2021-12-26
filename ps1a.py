# portion of the cost needed for a downpayment
portion_down_payment = 0.25

# annual rate
r = 0.04

# These are the inputs needed from the user
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

# monthly salary - calculated using user input
monthly_salary = float(annual_salary/12)

# Calculate the down payment
down_payment = float(total_cost*portion_down_payment)

#initialize current_savings variable
current_savings = float(0.00)

#initialize number of months variable
months = int(0)

# Set up a while loop to do the calculations
while current_savings<down_payment:
    current_savings = current_savings + (portion_saved*monthly_salary) + (current_savings*(r/12))
    months = months + 1


print("Number of months: ", months)
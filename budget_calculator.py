# Budget Calculator
print("Welcome to your Budgetting Calculator!!!")

# Get Income
income = float((input("Please Enter Your Income below:\n$")))

# Initial Expenses 
expenses = float(input("Please Enter Your Total Expenses below:\n$"))

# Budget Calculation
remaining = income - expenses

# View Results
print(f"Your remaining budget is: ${remaining}")

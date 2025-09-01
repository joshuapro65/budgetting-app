# Budget Calculator
print("Welcome to your Budgeting Calculator!!!")

# Get Income
income = float((input("Please Enter Your Income below:\n$")))

# Initial Expenses 
expense_for = input("Please Enter What The Expense is For:\n")
expenses = float(input("Please Enter the Cost of your Expenses:\n$"))
other_expenses_for = input("Are there any other expenses that you wish to enter?\nPlease enter Y for Yes or N for No.")

                        
if other_expenses_for == "Y":
    other_expenses = input("Please enter what the Expense is for:\n")
    other_expenses_cost = float(input(f"Please enter the cost of the Expense: $"))
    expenses = other_expenses_cost + expenses

if other_expenses_for == "N":
    expenses = expenses


# Budget Calculation
remaining = income - expenses

# View Results
print(f"Your total expenses will be ${expenses}, these will be for {expense_for}.\n")
print(f"Your remaining budget is: ${remaining}")

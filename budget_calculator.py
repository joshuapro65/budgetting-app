# Budget Calculator
print("Welcome to your Budgeting Calculator!!!")

# Get Income
income = float((input("Please Enter Your Income below:\n$")))

# Initial Expenses 
expense_for = [input("Please Enter What The Expense is For:\n")]
expenses = float(input("Please Enter the Cost of your Expenses:\n$"))

# Checks if you have enough money for your expenses
if income < expenses:
    print("You don't have enough money for this!!!")
    exit()


# Addition of another or multiple expenses
other_expenses_for = input("Are there any other expenses that you wish to enter?\nPlease enter Y for Yes or N for No.\n").upper()


# While loop to continue asking if the user wants to add another expense
while True:
    if other_expenses_for == "Y":
        expense_for.append(input("Please enter what the Expense is for:\n"))
        other_expenses_cost = float(input(f"Please enter the cost of the Expense:\n$"))
        expenses += other_expenses_cost

        other_expenses_for = input("Are there any other expenses that you wish to enter?\nPlease enter Y for Yes or N for No.\n").upper() # makes it so that the user's input doesn't give an error for a y entry

    elif other_expenses_for == "N":
        print("Processing your data......")
        break
    else:
        other_expenses_for = input("You entered and invalid input. Please enter Y for Yes or N for No!!!\n").upper() # checks the user's input to see if there was invalid entries 

# Budget Calculation
remaining = income - expenses

# Checks if your expenses are more than what you have allocated
if remaining <= 0:
    print("You will exceed your total income...")
    cont = input("Do you want to continue? Please enter Y for Yes or N for No.\n").upper()
    if cont == "Y":
        print("Ok")
    elif cont == "N":
        print("Ok")
        exit()

# View Results
print("\n")
print(f"Your total expenses will be ${expenses}, these will be for {expense_for}: {expenses}.\n")
print(f"Your remaining budget is: ${remaining}")

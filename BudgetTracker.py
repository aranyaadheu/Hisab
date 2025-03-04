# BUDGET TRACKER
# Tracks expenses and shows total spent

# List to store expenses
expenses = []
print("Welcome to Budget Tracker!")

# Get expenses from user
while True:
    expense = input("Enter an expense (or 'done' to finish): ")
    if expense == 'done':
        break
    expenses.append(float(expense))  # Add as a number

# Calculate and show results
total = sum(expenses)  # Total spent
count = len(expenses)  # Number of expenses
print(f"\nYou entered {count} expenses.")
print(f"Total spent: ${total:.2f}")
print("Expenses:", expenses)
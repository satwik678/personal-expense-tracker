# Personal Expense Tracker

def get_total(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total

def get_highest_expense(expenses):
    highest = expenses[0]
    for expense in expenses:
        if expense["amount"] > highest["amount"]:
            highest = expense
    return highest

print("PERSONAL EXPENSE TRACKER")
print("-------------------------")

budget = float(input("Enter your monthly budget: ₹"))
count = int(input("Enter number of expenses: "))

expenses = []

for i in range(count):
    print("\nExpense", i + 1)
    category = input("Enter category: ")
    amount = float(input("Enter amount: ₹"))

    expenses.append({
        "category": category,
        "amount": amount
    })

total = get_total(expenses)
highest = get_highest_expense(expenses)
balance = budget - total

print("\n========== SUMMARY ==========")

for expense in expenses:
    print(expense["category"], ": ₹", format(expense["amount"], ".2f"))

print("-----------------------------")
print("Total Spending : ₹", format(total, ".2f"))
print("Highest Expense:", highest["category"], "- ₹", format(highest["amount"], ".2f"))

if balance >= 0:
    print("Budget Status  : Within budget")
    print("Remaining      : ₹", format(balance, ".2f"))
else:
    print("Budget Status  : Budget exceeded")
    print("Extra Spending : ₹", format(abs(balance), ".2f"))

print("=============================")
import calendar
import datetime
from expense import Expense

def main():
    print("Running Expense Tracker")
    expense_file_path = "expenses.csv"
    budget = 2000

    # get user input for expense
    expense = get_user_expense()

    # write their expense to a file
    save_expense_to_file(expense, expense_file_path)

    # read file and summarize expenses
    summarize_expense(expense_file_path, budget)

def get_user_expense():
    print("Getting user expenses")
    expense_name = input("Enter expense name: ")
    expense_amount = input("Enter expense amount: ")

    expense_category = [
        "Food", "Home", "Work", "Fun", "Misc"
    ]

    while True:
        print("Select an expense category: ")
        for i, category_name in enumerate(expense_category):
            print(f"  {i+1}. {category_name}")

        value_range = f"[1 - {len(expense_category)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if selected_index in range(len(expense_category)):
            selected_category = expense_category[selected_index]
            new_expense = Expense(name = expense_name, category = selected_category, amount = int(expense_amount))
            return new_expense
        else:
            print("Invalid category. Please try again.")

        break

def save_expense_to_file(expense, expense_file_path):
    print(f"Saving user expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name}, {expense.category}, {expense.amount}\n")

def summarize_expense(expense_file_path, budget):
    print("Summarizing user expenses")
    expenses = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_category, expense_amount = line.strip().split(",")
            line_expense = Expense(name = expense_name, category = expense_category, amount = float(expense_amount))
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("Expenses by category:")
    for key, amount in amount_by_category.items():
        print(f"   {key}: ${amount:.2f}")

    total_spent = sum([x.amount for x in expenses])
    print(f"Total spent: ${total_spent:.2f}")

    remaining_budget = budget - total_spent
    print(f"Budget remaining: ${remaining_budget:.2f}")

    #get remaining days
    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day

    daily_budget = remaining_budget / remaining_days
    print(green(f"Budget per day: ${daily_budget:.2f}"))

def green(text):
    return f"\033[92m{text}\033[0m"

if __name__ == "__main__":
    main()

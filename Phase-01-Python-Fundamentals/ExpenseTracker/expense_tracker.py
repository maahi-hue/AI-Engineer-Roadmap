from expense import Expense

def main():
    print("Running Expense Tracker")
    expense_file_path = "expenses.csv"

    # get user input for expense
    expense = get_user_expense()

    # write their expense to a file
    save_expense_to_file(expense, expense_file_path)

    # read file and summarize expenses
    summarize_expense(expense_file_path)

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

def summarize_expense(expense_file_path):
    print("Summarizing user expenses")

if __name__ == "__main__":
    main()

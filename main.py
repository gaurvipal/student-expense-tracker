import expense_manager
import analytics
import budget_manager
import validators
import utils


expenses = []
budgets = {}


utils.display_title()

while True:
    utils.display_menu()

    choice = input("Enter your choice: ").strip()

    if choice == "1": #code to add a expense
        print("\n---------- ADD EXPENSE ----------")

        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        description = input("Enter description: ")
        date = input("Enter date (YYYY-MM-DD): ")

        if not validators.validate_amount(amount):
            print("Invalid amount.")
            continue

        if not validators.validate_category(category):
            print("Invalid category.")
            continue

        if not validators.validate_date(date):
            print("Invalid date format.")
            continue

        message = expense_manager.add_expense(
            expenses,
            amount,
            category,
            description,
            date
        )

        print(message)

    elif choice == "2": #code to view the expenses
        expense_manager.view_expenses(expenses)

    elif choice == "3": #code to update a expense
        print("\n---------- UPDATE EXPENSE ----------")

        expense_id = int(input("Enter expense ID: "))
        amount = float(input("Enter new amount: "))
        category = input("Enter new category: ")
        description = input("Enter new description: ")
        date = input("Enter new date (YYYY-MM-DD): ")

        message = expense_manager.update_expense(
            expenses,
            expense_id,
            amount,
            category,
            description,
            date
        )

        print(message)

    elif choice == "4": #code to delete a expense
        print("\n---------- DELETE EXPENSE ----------")

        expense_id = int(input("Enter expense ID: "))

        message = expense_manager.delete_expense(
            expenses,
            expense_id
        )

        print(message)

    elif choice == "5": #code to search expenses
        print("\n---------- SEARCH EXPENSES ----------")

        keyword = input("Enter category, description, or date to search: ")

        results = expense_manager.search_expenses(
            expenses,
            keyword
        )

        utils.display_search_results(results)

    elif choice == "6": #code to find total expenses
        total = analytics.total_expenses(expenses)

        print("\n---------- TOTAL EXPENSES ----------")
        print("Total expenses: ₹", total)

    elif choice == "7": #code to find category summary
        summary = analytics.category_summary(expenses)

        print("\n---------- CATEGORY SUMMARY ----------")

        if len(summary) == 0:
            print("No expenses found.")
        else:
            for category in summary:
                print(category, ": ₹", summary[category])

    elif choice == "8": #code to find category summary  
        highest = analytics.highest_expense(expenses)

        print("\n---------- HIGHEST EXPENSE ----------")

        if highest is None:
            print("No expenses found.")
        else:
            print("Amount:", highest["amount"])
            print("Category:", highest["category"])
            print("Description:", highest["description"])
            print("Date:", highest["date"])

    elif choice == "9": #code for setting monthly budget
        print("\n---------- SET MONTHLY BUDGET ----------")

        month = input("Enter month (YYYY-MM): ")
        amount = float(input("Enter budget amount: "))

        message = budget_manager.set_budget(
            budgets,
            month,
            amount
        )

        print(message)

    elif choice == "10": #code for checking budget status
        print("\n---------- BUDGET STATUS ----------")

        month = input("Enter month (YYYY-MM): ")

        total = analytics.monthly_expenses(
            expenses,
            month
        )

        status = budget_manager.budget_status(
            budgets,
            month,
            total
        )

        print("Total spent:", total)
        print(status)

    elif choice == "11": #code to exit from the program 
        print("\nThank you for using Student Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")
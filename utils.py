def display_title():
    print("\n====================================")
    print("       STUDENT EXPENSE TRACKER")
    print("====================================")


def display_menu():
    print("\n---------- MENU ----------")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Search Expenses")
    print("6. Total Expenses")
    print("7. Category Summary")
    print("8. Highest Expense")
    print("9. Set Monthly Budget")
    print("10. Check Budget Status")
    print("11. Exit")
    print("--------------------------")


def display_expense(expense):
    print("ID:", expense["id"])
    print("Amount:", expense["amount"])
    print("Category:", expense["category"])
    print("Description:", expense["description"])
    print("Date:", expense["date"])


def display_search_results(results):
    if len(results) == 0:
        print("No matching expenses found.")
        return

    print("\n---------- SEARCH RESULTS ----------")

    for expense in results:
        display_expense(expense)
        print()


def display_category_summary(summary):
    if len(summary) == 0:
        print("No expenses found.")
        return

    print("\n---------- CATEGORY SUMMARY ----------")

    for category in summary:
        print(category, ":", "₹", summary[category])
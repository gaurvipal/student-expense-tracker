def add_expense(expenses, amount, category, description, date):
    new_expense_id = len(expenses) + 1

    new_expense = {
        "id": new_expense_id,
        "amount": amount,
        "category": category,
        "description": description,
        "date": date
    }

    expenses.append(new_expense)

    return "Expense was added successfully."


def view_expenses(expenses):
    if len(expenses) == 0:
        print("No expenses were found.")
        return

    print("\n---------- EXPENSES ----------")

    for expense in expenses:
        print(
            "ID:", expense["id"],
            "| Amount:", expense["amount"],
            "| Category:", expense["category"],
            "| Description:", expense["description"],
            "| Date:", expense["date"]
        )


def update_expense(expenses, expense_id, amount, category, description, date):
    for expense in expenses:
        if expense["id"] == expense_id:
            expense["amount"] = amount
            expense["category"] = category
            expense["description"] = description
            expense["date"] = date

            return "Expense was updated successfully."

    return "The Expense ID could not be located."


def delete_expense(expenses, expense_id):
    for expense in expenses:
        if expense["id"] == expense_id:
            expenses.remove(expense)

            return "Expense was deleted successfully."

    return "The Expense ID could not be located."


def search_expenses(expenses, keyword):
    search_results = []

    lower_case_keyword = keyword.lower()

    for expense in expenses:
        if (
            lower_case_keyword in expense["category"].lower()
            or lower_case_keyword in expense["description"].lower()
            or lower_case_keyword in expense["date"].lower()
        ):
            search_results.append(expense)

    return search_results
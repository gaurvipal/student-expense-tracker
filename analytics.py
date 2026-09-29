def total_expenses(expenses):
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    return total


def expense_count(expenses):
    count = 0

    for expense in expenses:
        count = count + 1

    return count


def category_summary(expenses):
    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in summary:
            summary[category] = summary[category] + amount
        else:
            summary[category] = amount

    return summary


def highest_expense(expenses):
    if len(expenses) == 0:
        return None

    highest = expenses[0]

    for expense in expenses:
        if expense["amount"] > highest["amount"]:
            highest = expense

    return highest


def monthly_expenses(expenses, month):
    total = 0

    for expense in expenses:
        if expense["date"].startswith(month):
            total = total + expense["amount"]

    return total
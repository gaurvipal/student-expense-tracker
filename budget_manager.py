def set_budget(budgets, month, amount):
    if amount <= 0:
        return "Budget must be greater than zero."

    budgets[month] = amount

    return "Budget set successfully."


def get_budget(budgets, month):
    if month in budgets:
        return budgets[month]

    return 0


def calculate_remaining(budgets, month, total_spent):
    budget = get_budget(budgets, month)

    if budget == 0:
        return None

    return budget - total_spent


def budget_status(budgets, month, total_spent):
    budget = get_budget(budgets, month)

    if budget == 0:
        return "No budget has been set for this month."

    remaining = budget - total_spent

    if remaining > 0:
        return "Within budget. Remaining: ₹" + str(remaining)

    elif remaining == 0:
        return "Budget limit reached."

    else:
        return "Budget exceeded by: ₹" + str(abs(remaining))
    
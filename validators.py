def validate_amount(amount):
    if amount > 0:
        return True
    else:
        return False


def validate_category(category):
    if len(category.strip()) > 0:
        return True
    else:
        return False


def validate_date(date):
    if len(date) != 10:
        return False

    if date[4] != "-" or date[7] != "-":
        return False

    year = date[0:4]
    month = date[5:7]
    day = date[8:10]

    if not year.isdigit():
        return False

    if not month.isdigit():
        return False

    if not day.isdigit():
        return False

    if int(month) < 1 or int(month) > 12:
        return False

    if int(day) < 1 or int(day) > 31:
        return False

    return True


def validate_month(month):
    if len(month) != 7:
        return False

    if month[4] != "-":
        return False

    year = month[0:4]
    month_number = month[5:7]

    if not year.isdigit():
        return False

    if not month_number.isdigit():
        return False

    if int(month_number) < 1 or int(month_number) > 12:
        return False

    return True
from datetime import datetime

def get_days_from_today(date):
    """ Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної."""
    try:
        correct_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        print(f"Неправильний формат дати: '{date}'.")
        return None
    today = datetime.today().date()
    result = today - correct_date
    return result.days

print(get_days_from_today("2021-05-05"))  # Example usage
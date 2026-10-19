import random

def get_numbers_ticket(min, max, quantity):
    """ Функція повертає випадковий набір чисел з quantity, причому всі випадкові числа в наборі унікальні в заданому діапазоні від min до max. Якщо параметри некоректні, повертає []."""
    if min < 1 or max > 1000 or min > max:
        print(f"Неправильний діапазон чисел: [{min}, {max}]. Діапазон повинен бути в межах [1, 1000] і min не повинен перевищувати max.")
        return []
    if quantity < 1 or quantity > (max - min + 1):
        print(f"Неправильна кількість чисел: {quantity}. Кількість повинна бути в межах [1, {max - min + 1}].")
        return []
    number_set = set()
    while len(number_set) < quantity:
        number_set.add(random.randint(min, max))
    return sorted(number_set)

print(get_numbers_ticket(1, 10, 5))  # Example usage

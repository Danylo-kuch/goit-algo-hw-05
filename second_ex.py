from typing import Callable

def generator_numbers(text: str):
    for word in text.split():
        try:
            money = float(word)
            yield money
        except ValueError:
            continue

def sum_profit(text: str, func: Callable):
    return sum(func(text))

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід працівника: {total_income}")

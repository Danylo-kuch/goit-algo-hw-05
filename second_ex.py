from typing import Callable
import re

def generator_numbers(text: str):
    pattern = r'(?<=\s)\d+\.\d+(?=\s)' #Дійсні числа у тексті вважаються записаними без помилок і чітко відокремлені пробілами з обох боків.
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    return sum(func(text))

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід працівника: {total_income}")

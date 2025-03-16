import re
from typing import Callable


def generator_numbers(text: str):
    """
    Extracts all numbers from the given text and yields them as floats.
    
    Args:
        text (str): The input text containing numbers.
    
    Yields:
        float: The next number found in the text.
    """
    pattern = r'\d+(?:[.,]\d+)?'
    for match in re.findall(pattern, text):
        yield float(match.replace(',', '.'))


def sum_profit(text: str, func: Callable) -> float:
    """
    Sums all the numbers extracted from the text using the provided function.
    
    Args:
        text (str): The input text containing numbers.
        func (Callable): A function that extracts numbers from the text.
    
    Returns:
        float: The sum of all extracted numbers.
    """
    return sum(func(text))



# tests
text = "The employee's total income consists of several parts: $1000.01 as the base income, supplemented by additional earnings of $27.45 and $324.00."
total_income = sum_profit(text, generator_numbers)

print(f"Total income: {total_income}") # Total income: 1351.46



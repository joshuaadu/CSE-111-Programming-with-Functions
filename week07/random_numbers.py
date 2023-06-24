"""
A program that creates a list of numbers, appends more numbers onto the list, and prints the list.
"""
import random


def main():
    numbers = [16.2, 75.1, 52.3]
    print(f"numbers {numbers}")
    append_random_numbers(numbers)
    print(f"numbers {numbers}")
    append_random_numbers(numbers, 3)
    print(f"numbers {numbers}")



def append_random_numbers(numbers_list: list, quantity = 1):
    for _ in range(quantity):
        number =round(random.uniform(1, 100), 1)
        numbers_list.append(number)


if __name__ == "__main__":
    main()
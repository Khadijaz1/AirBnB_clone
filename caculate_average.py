#!/usr/bin/python3
def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        return None

    total = sum(numbers)
    average = total / len(numbers)
    return average


def main():
    """Entry point of the program."""
    numbers = [1, 2, 3, 4, 5]
    result = calculate_average(numbers)
    print(f"The average is: {result}")


if name == "main":
    main()

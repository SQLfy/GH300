def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.

    Args:
        numbers (list of float or int): The list of numbers to calculate the average from.

    Returns:
        float: The average of the numbers. Returns 0 if the list is empty.
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

if __name__ == "__main__":
    sample_numbers = [10, 20, 30, 40, 50]
    average = calculate_average(sample_numbers)
    print(f"The average of {sample_numbers} is {average}")
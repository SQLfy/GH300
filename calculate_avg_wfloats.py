from typing import Iterable, List
import math


def _to_float_list(numbers: Iterable) -> List[float]:
    """Convert an iterable array of values to a list of floats.

    Raises:
        TypeError: if any element cannot be converted to float.
    """
    nums = list(numbers)  # materialize to handle generators and check emptiness
    try:
        return [float(x) for x in nums]
    except (TypeError, ValueError) as exc:
        raise TypeError("All items in 'numbers' must be numeric") from exc


def calculate_avg(numbers: Iterable) -> float:
    """Calculate the average of an iterable of numbers.

    Returns 0.0 if the iterable is empty.

    Raises:
        TypeError: if any element cannot be converted to float.
    """
    nums = _to_float_list(numbers)
    if not nums:
        return 0.0
    total = math.fsum(nums)
    return total / len(nums)

if __name__ == "__main__":
    sample_numbers = [10, 20, 30, 40, 50]
    average = calculate_avg(sample_numbers)
    print(f"The average of {sample_numbers} is {average}")

    sample_floats = [10.2, 20.2, 30.2, 40.2, 50.2]
    average = calculate_avg(sample_floats)
    print(f"The average of {sample_floats} is {average}")
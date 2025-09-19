from typing import Iterable
import math


def calculate_avg(numbers: Iterable[float]) -> float:
    """
    Calculate the average of an iterable of numbers.

    Returns 0.0 if the iterable is empty.

    Raises:
        TypeError: if any element cannot be converted to float.
    """
    nums = list(numbers)  # materialize to handle generators and check emptiness
    if not nums:
        return 0.0
    try:
        total = math.fsum(float(x) for x in nums)
    except (TypeError, ValueError) as exc:
        raise TypeError("All items in 'numbers' must be numeric") from exc
    return total / len(nums)

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

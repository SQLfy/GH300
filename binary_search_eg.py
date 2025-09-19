def binary_search(arr, target):
    """
    Perform binary search on a sorted array.

    Args:
        arr (list): Sorted list of elements.
        target: Element to search for.

    Returns:
        int: Index of target if found, else -1.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
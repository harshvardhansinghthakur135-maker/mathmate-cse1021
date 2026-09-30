"""Module 3 - Array & List Analyzer.

Course concepts (Unit 5 - Array Techniques and Python Lists): array order reversal,
array counting, finding the maximum, removal of duplicates from an ordered array,
partitioning an array, finding the Kth smallest element, tuples, sets, dictionaries.
"""


def reverse_array(numbers):
    """Reverse a list by swapping from both ends (returns a new list)."""
    result = list(numbers)
    left, right = 0, len(result) - 1
    while left < right:
        result[left], result[right] = result[right], result[left]
        left += 1
        right -= 1
    return result


def count_occurrences(numbers, target):
    """How many times `target` appears in the list."""
    count = 0
    for value in numbers:
        if value == target:
            count += 1
    return count


def find_max(numbers):
    """Largest element (linear scan)."""
    if len(numbers) == 0:
        raise ValueError("List is empty.")
    largest = numbers[0]
    for value in numbers:
        if value > largest:
            largest = value
    return largest


def find_min(numbers):
    """Smallest element (linear scan)."""
    if len(numbers) == 0:
        raise ValueError("List is empty.")
    smallest = numbers[0]
    for value in numbers:
        if value < smallest:
            smallest = value
    return smallest


def remove_duplicates_sorted(numbers):
    """Remove duplicates from an ORDERED list in one pass."""
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i - 1]:
            raise ValueError("List must be sorted in ascending order.")
    if len(numbers) == 0:
        return []
    unique = [numbers[0]]
    for value in numbers[1:]:
        if value != unique[-1]:
            unique.append(value)
    return unique


def partition(numbers, pivot):
    """Split into (less than pivot, equal to pivot, greater than pivot)."""
    less, equal, greater = [], [], []
    for value in numbers:
        if value < pivot:
            less.append(value)
        elif value == pivot:
            equal.append(value)
        else:
            greater.append(value)
    return less, equal, greater


def kth_smallest(numbers, k):
    """Kth smallest element (1 = smallest) by repeatedly removing the minimum."""
    if k < 1 or k > len(numbers):
        raise ValueError(f"k must be between 1 and {len(numbers)}.")
    remaining = list(numbers)
    smallest = None
    for _ in range(k):
        smallest = find_min(remaining)
        remaining.remove(smallest)
    return smallest


def frequency_table(numbers):
    """Dictionary {value: how many times it occurs}."""
    table = {}
    for value in numbers:
        table[value] = table.get(value, 0) + 1
    return table


def set_operations(first, second):
    """Union, intersection and difference of two lists using Python sets."""
    a, b = set(first), set(second)
    return {
        "union": sorted(a | b),
        "intersection": sorted(a & b),
        "difference": sorted(a - b),
    }


def summary(numbers):
    """Basic statistics for a list of numbers, returned as a dictionary."""
    if len(numbers) == 0:
        raise ValueError("List is empty.")
    total = 0
    for value in numbers:
        total += value
    return {
        "count": len(numbers),
        "sum": total,
        "mean": round(total / len(numbers), 2),
        "maximum": find_max(numbers),
        "minimum": find_min(numbers),
        "distinct": len(set(numbers)),
    }

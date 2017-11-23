"""
You have k lists of sorted integers. Find the smallest range that includes at least one number from each of the k lists.

For example,
List 1: [4, 10, 15, 24, 26]
List 2: [0, 9, 12, 20]
List 3: [5, 18, 22, 30]

The smallest range here would be [20, 24] as it contains 24 from list 1, 20 from list 2, and 22 from list 3.

"""
import heapq


def find_minimum_range(sequences):
    # Maintain information which sequence each item belongs to
    sequences = [[(item, n) for item in seq] for n, seq in enumerate(sequences)]
    # Merge sequences into a single minheap, taking advantage of already sorted lists
    heap = heapq.merge(*sequences)
    # Current items to test
    found_range = None
    last_range = None
    current_items = [None] * len(sequences)
    for item, n in heap:
        current_items[n] = item
        if not all(current_items): # List not yet filled
            continue
        # Find range of current selection
        minimum = min(current_items)
        maximum = max(current_items)
        current_range = abs( maximum -minimum)
        # Update minimum range
        if not last_range or current_range < last_range:
            found_range = [minimum, maximum]
            last_range = current_range

    return found_range
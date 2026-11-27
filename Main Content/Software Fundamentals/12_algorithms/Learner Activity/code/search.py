# Linear search vs binary search on the list from Study Guide p. 78.

numbers = [3, 8, 12, 15, 20, 24, 29, 33, 37, 41, 46, 52, 58, 63, 70]


def linear_search(items, target):
    checks = 0
    for i, value in enumerate(items):
        checks += 1
        if value == target:
            return i, checks
    return -1, checks


def binary_search(items, target):
    # Only works if items is sorted.
    low, high = 0, len(items) - 1
    checks = 0
    while low <= high:
        middle = (low + high) // 2
        checks += 1
        print(f"  check {checks}: middle is {items[middle]}")
        if items[middle] == target:
            return middle, checks
        if items[middle] < target:
            low = middle + 1      # keep the right half
        else:
            high = middle - 1     # keep the left half
    return -1, checks


print("Linear search for 37:", linear_search(numbers, 37)[1], "checks")
print("Binary search for 37:")
print("  found after", binary_search(numbers, 37)[1], "checks")

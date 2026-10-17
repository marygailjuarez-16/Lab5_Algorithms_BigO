
# EXERCISE 1: EMERGENCY DISPATCH RECORD SEARCH

import time

# Student-specific inputs
LAST_NAME = "Juarez"
STUDENT_ID = "TUPM-26-1843"
FAVORITE_ARTIST = "Arthur Nery"

SEED_DIGIT = int(STUDENT_ID[-1])
ID_SUM = sum(int(digit) for digit in STUDENT_ID if digit.isdigit())
NAME_LENGTH = len(LAST_NAME)
ARTIST_LENGTH = len(FAVORITE_ARTIST)
ARTIST_SUM = sum(
    ord(letter.upper()) - ord("A") + 1
    for letter in FAVORITE_ARTIST
    if letter.isalpha()
)

# Generate original incident records
original_records = [
    ID_SUM * 10 + ARTIST_SUM + i * SEED_DIGIT
    for i in range(10)
]

# Rotate the records using SEED_DIGIT
rotation_point = SEED_DIGIT % len(original_records)

rotated_records = (
    original_records[rotation_point:]
    + original_records[:rotation_point]
)

# Generate the target using ID_SUM and ARTIST_SUM
target_index = (ID_SUM + ARTIST_SUM) % len(original_records)
target = original_records[target_index]


# Binary search for a rotated sorted list
def rotated_binary_search(data, target):
    low = 0
    high = len(data) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2

        comparisons += 1
        if data[mid] == target:
            return mid, comparisons

        comparisons += 1
        if data[low] <= data[mid]:
            comparisons += 1
            if data[low] <= target:
                comparisons += 1
                if target < data[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                low = mid + 1

        else:
            comparisons += 1
            if data[mid] < target:
                comparisons += 1
                if target <= data[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                high = mid - 1

    return -1, comparisons


# Linear search
def linear_search(data, target):
    comparisons = 0

    for index, value in enumerate(data):
        comparisons += 1

        if value == target:
            return index, comparisons

    return -1, comparisons


# Measure binary search execution time
start = time.perf_counter()
binary_position, binary_comparisons = rotated_binary_search(
    rotated_records, target
)
binary_time = time.perf_counter() - start

# Measure linear search execution time
start = time.perf_counter()
linear_position, linear_comparisons = linear_search(
    rotated_records, target
)
linear_time = time.perf_counter() - start

# Display results
print("EXERCISE 1: EMERGENCY DISPATCH RECORD SEARCH")
print("Student:", LAST_NAME)
print("Student ID:", STUDENT_ID)
print("Favorite Artist:", FAVORITE_ARTIST)
print("SEED_DIGIT:", SEED_DIGIT)
print("ID_SUM:", ID_SUM)
print("ARTIST_SUM:", ARTIST_SUM)

print("\nOriginal Dataset:", original_records)
print("Rotation Point:", rotation_point)
print("Rotated Dataset:", rotated_records)
print("Target Incident:", target)

print("\nBinary Search Position:", binary_position)
print("Binary Search Comparisons:", binary_comparisons)
print(f"Binary Search Time: {binary_time:.8f} seconds")

print("\nLinear Search Position:", linear_position)
print("Linear Search Comparisons:", linear_comparisons)
print(f"Linear Search Time: {linear_time:.8f} seconds")

print("\nTime Complexity:")
print("Rotated Binary Search: O(log n)")
print("Linear Search: O(n)")

print("\nAuxiliary Space Complexity:")
print("Both search functions: O(1)")

print("\nTarget Found:", binary_position != -1)
print("Search Results Match:", binary_position == linear_position)


# EXERCISE 2: UNIVERSITY ENROLLMENT RECORDS

import time

# Student-specific inputs
LAST_NAME = "Juarez"
STUDENT_ID = "TUPM-26-1843"
FAVORITE_ARTIST = "Arthur Nery"

SEED_DIGIT = int(STUDENT_ID[-1])
ID_SUM = sum(int(digit) for digit in STUDENT_ID if digit.isdigit())
NAME_LENGTH = len(LAST_NAME)
ARTIST_LENGTH = len(FAVORITE_ARTIST)

# Generate sorted enrollment datasets
dataset_a = [
    ID_SUM + i * SEED_DIGIT
    for i in range(10)
]

dataset_b = [
    NAME_LENGTH + ARTIST_LENGTH + i * SEED_DIGIT
    for i in range(8)
]


# Merge two sorted datasets
def merge_sorted_datasets(a, b):
    i = 0
    j = 0
    merged = []
    comparisons = 0

    while i < len(a) and j < len(b):
        comparisons += 1

        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    # Copy the remaining elements
    while i < len(a):
        merged.append(a[i])
        i += 1

    while j < len(b):
        merged.append(b[j])
        j += 1

    return merged, comparisons


# Measure execution time
start = time.perf_counter()
consolidated, comparisons = merge_sorted_datasets(
    dataset_a, dataset_b
)
elapsed_time = time.perf_counter() - start

# Verify the result
total_before = len(dataset_a) + len(dataset_b)
total_after = len(consolidated)
is_sorted = all(
    consolidated[i] <= consolidated[i + 1]
    for i in range(len(consolidated) - 1)
)

# Display results
print("EXERCISE 2: UNIVERSITY ENROLLMENT RECORDS")
print("Student:", LAST_NAME)
print("Student ID:", STUDENT_ID)
print("SEED_DIGIT:", SEED_DIGIT)
print("ID_SUM:", ID_SUM)
print("NAME_LENGTH:", NAME_LENGTH)
print("ARTIST_LENGTH:", ARTIST_LENGTH)

print("\nDataset A:", dataset_a)
print("Dataset B:", dataset_b)
print("Consolidated Dataset:", consolidated)

print("\nRecords Before Consolidation:", total_before)
print("Records After Consolidation:", total_after)
print("Number of Comparisons:", comparisons)
print(f"Execution Time: {elapsed_time:.8f} seconds")

print("\nOrdering Verification:", is_sorted)
print("Record Count Verification:", total_before == total_after)

print("\nTime Complexity: O(n + m)")
print("Auxiliary Space Complexity: O(n + m)")

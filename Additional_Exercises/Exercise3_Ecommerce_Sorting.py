
# EXERCISE 3: E-COMMERCE ORDER PROCESSING

import random
import time

# Student-specific inputs
LAST_NAME = "Juarez"
STUDENT_ID = "TUPM-26-1843"
FAVORITE_ARTIST = "Arthur Nery"

SEED_DIGIT = int(STUDENT_ID[-1])
ID_SUM = sum(int(digit) for digit in STUDENT_ID if digit.isdigit())
NAME_LENGTH = len(LAST_NAME)

ARTIST_SUM = sum(
    ord(letter.upper()) - ord("A") + 1
    for letter in FAVORITE_ARTIST
    if letter.isalpha()
)

# Generate the original order dataset
orders = [
    ((ID_SUM * 7 + ARTIST_SUM + i * SEED_DIGIT) % 997) + 1
    for i in range(30)
]

# Generate three input conditions from the same orders
sorted_orders = sorted(orders)
reverse_orders = sorted(orders, reverse=True)

random_orders = orders.copy()
random.Random(ID_SUM + SEED_DIGIT + ARTIST_SUM).shuffle(
    random_orders
)

input_conditions = {
    "Sorted": sorted_orders,
    "Reverse": reverse_orders,
    "Random": random_orders
}


# Bubble Sort
def bubble_sort(data):
    a = data.copy()
    comparisons = 0
    movements = 0

    for i in range(len(a)):
        swapped = False

        for j in range(len(a) - i - 1):
            comparisons += 1

            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                movements += 3
                swapped = True

        if not swapped:
            break

    return a, comparisons, movements


# Selection Sort
def selection_sort(data):
    a = data.copy()
    comparisons = 0
    movements = 0

    for i in range(len(a) - 1):
        minimum = i

        for j in range(i + 1, len(a)):
            comparisons += 1

            if a[j] < a[minimum]:
                minimum = j

        if minimum != i:
            a[i], a[minimum] = a[minimum], a[i]
            movements += 3

    return a, comparisons, movements


# Insertion Sort
def insertion_sort(data):
    a = data.copy()
    comparisons = 0
    movements = 0

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0:
            comparisons += 1

            if a[j] > key:
                a[j + 1] = a[j]
                movements += 1
                j -= 1
            else:
                break

        a[j + 1] = key
        movements += 1

    return a, comparisons, movements


sorting_algorithms = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort
}

# Run every algorithm on every input condition
print("EXERCISE 3: E-COMMERCE ORDER PROCESSING")
print("Student:", LAST_NAME)
print("Student ID:", STUDENT_ID)
print("SEED_DIGIT:", SEED_DIGIT)
print("ID_SUM:", ID_SUM)
print("ARTIST_SUM:", ARTIST_SUM)

print("\nOriginal Order Dataset:", orders)
print("Dataset Size:", len(orders))

all_results = []

for condition, data in input_conditions.items():
    print(f"\n{'=' * 60}")
    print("INPUT CONDITION:", condition)
    print("Input Orders:", data)

    for algorithm_name, algorithm in sorting_algorithms.items():
        start = time.perf_counter()
        sorted_result, comparisons, movements = algorithm(data)
        elapsed_time = time.perf_counter() - start

        verified = sorted_result == sorted(data)

        result = {
            "condition": condition,
            "algorithm": algorithm_name,
            "comparisons": comparisons,
            "movements": movements,
            "time": elapsed_time,
            "verified": verified
        }

        all_results.append(result)

        print(f"\nAlgorithm: {algorithm_name}")
        print("Sorted Orders:", sorted_result)
        print("Comparisons:", comparisons)
        print("Movements:", movements)
        print(f"Execution Time: {elapsed_time:.8f} seconds")
        print("Sorting Verification:", verified)

# Summary table
print("\n" + "=" * 85)
print("SORTING PERFORMANCE COMPARISON")
print(
    f"{'Condition':<12}"
    f"{'Algorithm':<18}"
    f"{'Comparisons':>13}"
    f"{'Movements':>12}"
    f"{'Time (s)':>14}"
    f"{'Verified':>12}"
)

for result in all_results:
    print(
        f"{result['condition']:<12}"
        f"{result['algorithm']:<18}"
        f"{result['comparisons']:>13}"
        f"{result['movements']:>12}"
        f"{result['time']:>14.8f}"
        f"{str(result['verified']):>12}"
    )

# Big O analysis
print("\nBIG O ANALYSIS")
print("Bubble Sort: Best O(n), Average O(n^2), Worst O(n^2)")
print("Selection Sort: Best O(n^2), Average O(n^2), Worst O(n^2)")
print("Insertion Sort: Best O(n), Average O(n^2), Worst O(n^2)")

print("\nAuxiliary Space Complexity:")
print("All three sorting algorithms: O(n) including the copied list.")
print("The sorting operations themselves use O(1) extra space.")

import time
import random

# Алгоритмы сортировки
# Сортировка пузырьком (O(n^2))
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Сортировка выбором (O(n^2))
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# Сортировка слиянием (O(n log n))
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Линейный поиск (O(n))
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Бинарный поиск (O(log n))
def binary_search(arr, target):
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


# Функция для замера времени выполнения
def measure_time(func, *args):
    start_time = time.perf_counter()
    func(*args)
    end_time = time.perf_counter()
    return end_time - start_time


# Основная часть программы
sizes = [10 ** i for i in range(1, 8)]  # Размеры от 10 до 10 миллионов

print("Сортировка:")
print(f"{'Размер':<10} {'Пузырьком':<15} {'Выбором':<15} {'Слиянием':<15}")
for size in sizes:
    random_array = [random.randint(0, 10000000) for _ in range(size)]

    bubble_time = measure_time(bubble_sort, random_array.copy())
    selection_time = measure_time(selection_sort, random_array.copy())
    merge_time = measure_time(merge_sort, random_array.copy())

    print(f"{size:<10} {bubble_time:<15.6f} {selection_time:<15.6f} {merge_time:<15.6f}")

print("\nПоиск:")
print(f"{'Размер':<10} {'Линейный':<15} {'Бинарный':<15}")
for size in sizes:
    sorted_array = sorted([random.randint(0, 10000000) for _ in range(size)])

    linear_search_target = random.choice(sorted_array)
    linear_time = measure_time(linear_search, sorted_array, linear_search_target)

    binary_search_target = random.choice(sorted_array)
    binary_time = measure_time(binary_search, sorted_array, binary_search_target)

    print(f"{size:<10} {linear_time:<15.6f} {binary_time:<15.6f}")

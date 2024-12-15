import time


def custom_sort(arr):
    # Если список пустой или содержит один элемент, он считается отсортированным
    if len(arr) <= 1:
        return arr
    else:
        # Выбор среднего элемента
        mid_index = len(arr) // 2
        pivot = arr[mid_index]  # выбираем средний элемент

        # Разделение на элементы меньше и больше опорного
        left = [x for x in arr if x < pivot]
        right = [x for x in arr if x > pivot]

        # Рекурсивная сортировка левой и правой части
        return custom_sort(left) + [pivot] + custom_sort(right)


# Генерация массива длиной 1000 элементов, отсортированного в обратном порядке
array_length = 1000
array = list(range(array_length, 0, -1))

# Замер времени выполнения
start_time = time.time()
sorted_array = custom_sort(array)
end_time = time.time()

# Вывод отсортированного массива и времени выполнения
print("Отсортированный массив:", sorted_array)
print("Время выполнения:", end_time - start_time, "секунд")
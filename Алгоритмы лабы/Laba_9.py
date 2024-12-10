def heapify(arr, n, i):
    largest = i  # Инициализируем наибольший элемент как корень
    left = 2 * i + 1     # левый = 2*i + 1
    right = 2 * i + 2    # правый = 2*i + 2

    # Если левый дочерний элемент больше корня
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Если правый дочерний элемент больше, чем самый большой на данный момент
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Если самый большой элемент не корень
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Обмен

        # Рекурсивно хипируем затронутое поддерево
        heapify(arr, n, largest)

def sort(arr):
    n = len(arr)

    # Построение хипа (перегруппировка массива)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Один за другим извлекаем элементы из хипа
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Перемещаем текущий корень в конец
        heapify(arr, i, 0)

# Пример использования
arr = [12, 11, 13, 5, 6, 7]
sort(arr)
print(arr)
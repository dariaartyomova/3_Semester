#поразрядная сортировка
def c_sort(arr, p):
    n = len(arr)
    ex = [0] * n  # Выходной массив
    count = [0] * 10  # Счетчик для цифр (0-9)

    # Подсчет количества вхождений каждой цифры
    for i in range(n):
        index = arr[i] // p
        count[index % 10] += 1

    # Изменяем count[i], чтобы count[i] содержал позицию этого разряда в output
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Строим выходной массив
    for i in range(n - 1, -1, -1):
        index = arr[i] // p
        ex[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1

    # Копируем отсортированные элементы обратно в оригинальный массив
    for i in range(n):
        arr[i] = ex[i]

def sort(arr):
    # Находим максимальное число, чтобы определить количество разрядов
    max_num = max(arr)

    # Выполняем подсчет по каждому разряду
    exp = 1
    while max_num // exp > 0:
        c_sort(arr, exp)
        exp *= 10

# Пример использования
arr = [170, 45, 75, 90, 802, 24, 2, 66]
sort(arr)
print(arr)
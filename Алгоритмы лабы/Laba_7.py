#сортировка шелла
def sort(arr):
    n = len(arr)
    step = n // 2  # Начальный промежуток

    while step > 0:
        # Выполняем сортировку с текущим промежутком
        for i in range(step, n):
            x = arr[i]
            j = i - step
            while j >= 0 and x < arr[j]:
                arr[j + step] = arr[j]
                j -= step
            arr[j + step] = x  # вставляем x на нужную позицию

        step //= 2  # Уменьшаем промежуток

    return arr


# Пример использования
arr = [12, 34, 54, 2, 3]
sorted_arr = sort(arr)
print(sorted_arr)

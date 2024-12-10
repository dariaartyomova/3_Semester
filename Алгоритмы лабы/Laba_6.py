#сортировка выбором

def sort(arr):
    # Проходим по всему массиву
    for i in range(len(arr)):
        # Находим минимальный элемент в оставшейся части массива
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        # Меняем местами найденный минимальный элемент с первым элементом
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

n = [64, 34, 25, 12, 22, 11, 90]
print(sort(n))
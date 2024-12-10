#сортровка слиянием
def merge(left, right):
    result = []
    i = j = 0

    # Сравниваем элементы из левой и правой части и объединяем их
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Добавляем оставшиеся элементы
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2  # Находим середину массива
    left_half = sort(arr[:mid])  # Сортируем левую половину
    right_half = sort(arr[mid:])  # Сортируем правую половину

    return merge(left_half, right_half)  # Объединяем отсортированные половины


# Пример использования
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = sort(arr)
print( sorted_arr)
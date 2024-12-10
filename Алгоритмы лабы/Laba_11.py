#быстрая сортировка
def quick_sort(arr):
    # Если массив содержит 1 или 0 элементов, он уже отсортирован
    if len(arr) <= 1:
        return arr

    # Выбираем опорный элемент, здесь выбираем последний элемент
    op = arr[-1]


    left = [x for x in arr[:-1] if x <= op]
    right = [x for x in arr[:-1] if x > op]

    # Рекурсивно сортируем подмассивы и объединяем их с опорным элементом
    return quick_sort(left) + [op] + quick_sort(right)

arr = [38, 27, 43, 3, 9, 82, 111]
sorted_arr = quick_sort(arr)
print(sorted_arr)
#сортировка методом прочесывания
def sort(arr):
    step = len(arr)
    n = len(arr)
    # Проходим по всем элементам массива
    flag = 0
    while step > 1 or flag == 1:
        if step > 1:
            step = int(step/1.27)
        flag = 0
        i = 0
        # Последние i элементов уже отсортированы
        while step+i < n:
            if (arr[i] > arr[i + step]):  # Если текущий элемент больше элемента на расстоянии шага
                arr[i], arr[i + step] = arr[i + step], arr[i]  # Меняем их местами
                flag = 1 # Устанавливаем флаг перестановки
            i += step
    return arr

mas = [64, 34, 25, 12, 22, 11, 90]
print(sort(mas))

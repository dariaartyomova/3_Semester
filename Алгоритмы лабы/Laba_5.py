#метод вставки
def sort(arr):
    for i in range(1, len(arr)):
        x = arr[i]
        j = i - 1
        while j >= 0 and x < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = x #вставляем x на нужную позицию
    return arr

numbers = [64, 34, 25, 12, 22, 11, 90]
print("Отсортированная последовательность:", sort(numbers))


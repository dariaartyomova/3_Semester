import heapq
import os


# Разделение данных на блоки

def sort(arr):
    for i in range(1, len(arr)):
        x = arr[i]
        j = i - 1
        while j >= 0 and x < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = x #вставляем x на нужную позицию
    return arr
def split_file(input_file, block_size):
    block_number = 0
    with open(input_file, 'r') as infile:

        data = infile.readlines()
        while data:
            # Берем блок данных, который помещается в память
            block = data[:block_size]
            data = data[block_size:]

            # Сортируем блок
            sort(block)

            # Записываем отсортированный блок в новый файл
            block_filename = f'block_{block_number}.txt'
            with open(block_filename, 'w') as block_file:
                block_file.writelines(block)

            block_number += 1
    return block_number


# Многофазное слияние блоков
def merge_blocks(block_count):
    # Открываем все блоки для слияния
    open_files = []
    for i in range(block_count):
        block_filename = f'block_{i}.txt'
        open_files.append(open(block_filename, 'r'))

    # Используем кучу для слияния блоков
    merged_file = 'output.txt'
    with open(merged_file, 'w') as outfile:
        heap = []

        # Инициализируем кучу с первыми элементами каждого блока
        for i, file in enumerate(open_files):
            line = file.readline()
            if line:
                heapq.heappush(heap, (line.strip(), i))  # (значение, номер файла)

        # Слияние
        while heap:
            val, file_index = heapq.heappop(heap)
            outfile.write(val + '\n')  # Записываем результат в финальный файл

            # Читаем следующий элемент из того же блока
            next_line = open_files[file_index].readline()
            if next_line:
                heapq.heappush(heap, (next_line.strip(), file_index))

    # Закрываем все файлы
    for file in open_files:
        file.close()

    # Удаляем временные блоки
    for i in range(block_count):
        os.remove(f'block_{i}.txt')


# Основная функция
def external_sort(input_file, block_size):
    print(f"Разбиение файла {input_file} на блоки...")
    block_count = split_file(input_file, block_size)
    print(f"Слияние блоков в один файл...")
    merge_blocks(block_count)
    print("Сортировка завершена. Результат сохранен в 'output.txt'.")


# Ввод данных
input_file = 'input.txt'  # Исходный файл
block_size = 50  # Размер блока для обработки в памяти (количество строк)

# Запуск внешней сортировки
external_sort(input_file, block_size)


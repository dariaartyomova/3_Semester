import string
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def hash(key, table_size):
    # Простой способ хеширования строки
    return sum(ord(char) for char in key) % table_size

def hash_table_n(words, table_size):
    table = [None] * table_size
    for word in words:
        index = hash(word, table_size)
        original_index = index
        while table[index] is not None:
            index = (index + 1) % table_size
            if index == original_index:
                raise Exception("Хеш-таблица переполнена")
        table[index] = word
    return table



def hash_table_l(words, table_size):
    table = [[] for _ in range(table_size)]
    for word in words:
        index = hash(word, table_size)
        table[index].append(word)
    return table

def to_file(filename, table):
    with open(filename, 'w', encoding='utf-8') as file:
        for i, entry in enumerate(table):
            file.write(f"{i}: {entry}\n")



def main():
    input_file = 'input13-14.txt'

    output_file_open_addressing = 'output13.txt'
    output_file_chaining = 'output14.txt'

    table_size = 50  # Размер хеш-таблицы

    words = read_file(input_file)

    #13
    hash_table_nn = hash_table_n(words, table_size)
    to_file(output_file_open_addressing, hash_table_nn)

    #14
    hash_table_ll = hash_table_l(words, table_size)
    to_file(output_file_chaining, hash_table_ll)


if __name__ == '__main__':
    main()





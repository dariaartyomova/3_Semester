# создаем дерево
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def tree(s):
    def subtree(start):
        value = ''
        while start < len(s) and (s[start].isdigit() or s[start] == '-'):
            value += s[start]
            start += 1

        if not value:
            return None, start

        node = Node(int(value))

        # прямой обход(корень, правое поддерево, левое поддерево)
        if start < len(s) and s[start] == '(':
            start += 1
            node.left, start = subtree(start)
            if start < len(s) and s[start] == ',':
                start += 1
                node.right, start = subtree(start)
            if start < len(s) and s[start] == ')':
                start += 1

        return node, start

    tree, _ = subtree(0)
    return tree


# инициализируем ветки
def tree_to_string(node):
    if node is None:
        return ''

    left = tree_to_string(node.left)
    right = tree_to_string(node.right)

    if left or right:
        return f'{node.value}({left},{right})'
    else:
        return f'{node.value}'


# ищем значение вершины
def search(r, i):
    if r is None or r.value == i:
        return r

    if i < r.value:
        return search(r.left, i)
    else:
        return search(r.right, i)


# заменяем значение
def insert(r, i):
    if r is None:
        return Node(i)

    if i < r.value:
        r.left = insert(r.left, i)
    else:
        r.right = insert(r.right, i)

    return r


# удаляем значение корня и находим новый корень по приоритету
def delete(r, i):
    if r is None:
        return r

    if i < r.value:
        r.left = delete(r.left, i)
    elif i > r.value:
        r.right = delete(r.right, i)
    else:
        if r.left is None:
            return r.right
        elif r.right is None:
            return r.left

        min_node = find_min(r.right)
        r.value = min_node.value
        r.right = delete(r.right, min_node.value)

    return r


def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def menu():
    print("\n1. Поиск вершины")
    print("2. Добавление вершины")
    print("3. Удаление вершины")
    print("4. Выход")


def main():
    tree_string = '8(3(1,6(4,7)),10(,14(13,)))'

    root = tree(tree_string)

    while True:
        menu()
        choice = input("Выберите операцию: ")

        if choice == '1':
            key = int(input("Введите ключ для поиска: "))
            result = search(root, key)
            if result:
                print(f"Вершина {key} найдена.")
            else:
                print(f"Вершина {key} не найдена.")

        elif choice == '2':
            key = int(input("Введите ключ для добавления: "))
            root = insert(root, key)
            print(f"Вершина {key} добавлена.")

        elif choice == '3':
            key = int(input("Введите ключ для удаления: "))
            root = delete(root, key)
            print(f"Вершина {key} удалена.")

        elif choice == '4':
            print("\nДерево")
            print(tree_to_string(root))
            break

        else:
            print("Некорректный выбор. Попробуйте снова.")


if __name__ == '__main__':
    main()

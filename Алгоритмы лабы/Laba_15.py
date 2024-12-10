class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def tree_f(s):
    def subtree(i):
        value = ''
        while i < len(s) and (s[i].isdigit() or s[i] == '-'):
            value += s[i]
            i += 1

        if not value:
            return None, i

        node = Node(int(value))

        if i < len(s) and s[i] == '(':
            i += 1
            node.left, i = subtree(i)
            if i < len(s) and s[i] == ',':
                i += 1
                node.right,i = subtree(i)
            if i < len(s) and s[i] == ')':
                i += 1

        return node, i

    tree, _ = subtree(0)
    return tree


# Прямой обход
def straight(node):
    if node is None:
        return
    print(node.value, end=' ')
    straight(node.left)
    straight(node.right)


# Центральный обход
def center(node):
    if node is None:
        return
    center(node.left)
    print(node.value, end=' ')
    center(node.right)


# Концевой обход
def end(node):
    if node is None:
        return
    end(node.left)
    end(node.right)
    print(node.value, end=' ')


def main():
    tree_string = '8(3(1,6(4,7)),10(,14(13,)))'

    root = tree_f(tree_string)

    print("Прямой обход:")
    straight(root)
    print()

    print("Центральный обход:")
    center(root)
    print()

    print("Концевой обход:")
    end(root)
    print()


if __name__ == '__main__':
    main()
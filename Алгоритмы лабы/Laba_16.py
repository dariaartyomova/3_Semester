#нерекурсивный прямой обход
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


# Нерекурсивный прямой обход с использованием стека
def rek(root):
    if root is None:
        return ""

    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(str(node.value))

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return " ".join(result)


def main():
    tree_string = '8(3(1,6(4,7)),10(,14(13,)))'

    root = tree_f(tree_string)

    traversal_result = rek(root)
    print("Нерекурсивный прямой обход:")
    print(traversal_result)


if __name__ == '__main__':
    main()

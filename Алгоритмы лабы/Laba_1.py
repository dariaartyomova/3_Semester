import random
def check(string):
    stack = []
    equally = {')': '(', '}': '{', ']': '['}
    for i in string:
        if i in equally.values():
            stack.append(i)
        elif i in equally.keys():
            if len(stack) == 0 or stack.pop() != equally[i]:
                return False

    if len(stack) == 0:
        return True
    else:
        return False

print("Введите строку:")
text = input()
if check(text) is True:
    print("Строка существует")
else:
    print("Строка не существует")


print('6481\n' >= '4399\n')
#пример ввода данных
#())){][]]}
#{}{}[()]

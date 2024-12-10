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


def to_rpn(mth_ex):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    operators = []
    i = 0

    while i < len(mth_ex):
        char = mth_ex[i]

        # Распознаем отрицательные числа
        if char == '-' and (i == 0 or mth_ex[i - 1] in '(-+*/'):
            number = char
            i += 1
            while i < len(mth_ex) and mth_ex[i].isdigit():
                number += mth_ex[i]
                i += 1
            output.append(number)
            continue

        if char.isdigit():
            number = char
            while i + 1 < len(mth_ex) and mth_ex[i + 1].isdigit():
                i += 1
                number += mth_ex[i]
            output.append(number)
        elif char in precedence:
            while (operators and operators[-1] in precedence and
                   precedence[operators[-1]] >= precedence[char]):
                output.append(operators.pop())
            operators.append(char)
        elif char == '(':
            operators.append(char)
        elif char == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()  # удаляем '('
        i += 1

    while operators:
        output.append(operators.pop())

    return output


def evaluate_rpn(rpn):
    stack = []

    for i in rpn:
        if i.lstrip('-').isdigit():  # Учитываем отрицательные числа
            stack.append(int(i))
        else:
            b = stack.pop()
            a = stack.pop()

            if i == '+':
                stack.append(a + b)
            elif i == '-':
                stack.append(a - b)
            elif i == '*':
                stack.append(a * b)
            elif i == '/':
                if b == 0:
                    raise ZeroDivisionError("Деление на ноль")
                stack.append(a / b)

    return stack[0]


def evaluate_expression(mth_ex):
    mth_ex = mth_ex.replace('=', '')

    # Проверка скобок
    if not check(mth_ex):
        print("Некорректные скобки в выражении")
        return

    try:
        rpn = to_rpn(mth_ex)
        result = evaluate_rpn(rpn)
        print("Результат:", result)
    except ZeroDivisionError as e:
        print(e)
    except Exception as e:
        print("Ошибка:", e)


if __name__ == '__main__':
    expression = input("Введите математическое выражение: ")
    evaluate_expression(expression)

#пример ввода данных
#2+7*(3/9)-5=
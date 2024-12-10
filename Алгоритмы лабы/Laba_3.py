def find_numbers(x):
    results = set()  # Используем множество для уникальности
    k = 0
    while True:
        p_3 = 3 ** k
        if p_3 > x:
            break
        l = 0
        while True:
            p_5 = p_3 * (5 ** l)
            if p_5 > x:
                break
            m = 0
            while True:
                number = p_5 * (7 ** m)
                if number > x:
                    break
                results.add(number)
                m += 1
            l += 1
        k += 1

    return sorted(results)


x = int(input("Введите число x: "))
print(find_numbers(x))



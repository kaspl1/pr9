import random


def generate_random_list():
    l = random.randint(1, 20)
    return [random.randint(1, 100) for _ in range(l)]


def is_number(e):
    return isinstance(e, (int, float))


def are_all_elements_equal(y):
    for x in y:
        if x != y[0]:
            return False
    return True


def cyclic_shift_right(y):
    for x in y:
        if not is_number(x):
            print(f"Ошибка: элемент {x} не является числом.")
            return

    if not y:
        print("Список пуст.")
        return

    if len(y) == 1:
        print("В списке только один элемент")
        return

    if are_all_elements_equal(y):
        print("Все элементы в списке одинаковые.")
        return

    last = y[-1]
    for i in range(len(y) - 1, 0, -1):
        y[i] = y[i - 1]
    y[0] = last

    print("Список после циклического сдвига вправо:", y)


r = generate_random_list()

print("Сгенерированный список:", r)

cyclic_shift_right(r)
